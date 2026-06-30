"""End-to-end runner for JSON → MLIR → native executable examples."""

from __future__ import annotations

import re
import subprocess
import sys
import time
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from rich.console import Console
from rich.table import Table
from rich.text import Text

from xdsljson.pipeline.compiler import main as compile_main

EXPECT_PATTERN = re.compile(
    r"EXPECT(?:ED)?.*? '([^']*)'.*?'([^']*)'",
    re.IGNORECASE,
)

console = Console()


class ResultStats(Enum):
    OK = "Ok"
    ERROR = "Error"   # Crash of the program
    FAILED = "Failed" # Test failed


_STATUS_STYLES: dict[ResultStats, str] = {
    ResultStats.OK: "bold green",
    ResultStats.ERROR: "bold red",
    ResultStats.FAILED: "bold red",
}


@dataclass
class ResultInfo:
    name: str
    status: ResultStats
    message: str
    elapsed_s: float = 0.0


def discover_examples(project_root: Path) -> list[Path]:
    """Return main.json or main.py paths for each example subdirectory.

    Directories with a ``main.json`` are compiled via the JSON pipeline.
    Directories that only have a ``main.py`` (no ``main.json``) use the Python
    DSL to generate the binary directly.
    """
    examples_dir = project_root / "examples"
    paths: list[Path] = []
    for child in sorted(examples_dir.iterdir()):
        if not child.is_dir():
            continue
        if (child / "main.json").is_file():
            paths.append(child / "main.json")
        elif (child / "main.py").is_file():
            paths.append(child / "main.py")
    return paths


def _parse_expectations(stdout: str) -> tuple[list[tuple[str, str]], int]:
    """Return mismatches parsed from stdout."""
    mismatches: list[tuple[str, str]] = []
    n_tests = 0
    for line in stdout.splitlines():
        match = EXPECT_PATTERN.search(line)
        if match is None:
            continue
        expected, got = match.group(1), match.group(2)
        if expected != got:
            mismatches.append((expected, got))
        n_tests += 1
    return (mismatches, n_tests)


def run_example(input_path: Path, project_root: Path) -> ResultInfo:
    """Compile and run an example, then check EXPECT lines.

    Accepts either a ``main.json`` (JSON pipeline) or a ``main.py`` (Python
    DSL pipeline) as *input_path*.
    """
    start = time.perf_counter()
    name = input_path.parent.name
    project_root = project_root.resolve()
    input_path = input_path.resolve()
    file_runnable = input_path.with_suffix(".out")

    if input_path.suffix == ".py":
        # Python DSL: run the script directly; it calls compiler() internally.
        try:
            proc_compile = subprocess.run(
                [
                    sys.executable,
                    str(input_path),
                    "--project-root",
                    str(project_root),
                ],
                capture_output=True,
                text=True,
                timeout=120,
                check=False,
            )
        except Exception as exc:
            return ResultInfo(
                name=name,
                status=ResultStats.ERROR,
                message=str(exc) or repr(exc),
                elapsed_s=time.perf_counter() - start,
            )

        if proc_compile.returncode != 0:
            rc = proc_compile.returncode
            detail = proc_compile.stderr.strip() or f"exit code {rc}"
            return ResultInfo(
                name=name,
                status=ResultStats.ERROR,
                message=detail,
                elapsed_s=time.perf_counter() - start,
            )

    else:
        # JSON pipeline
        json_path = input_path
        try:
            exit_code = compile_main(
                [
                    str(json_path),
                    "--project-root",
                    str(project_root),
                    "--link",
                ]
            )

        # Exit code
        except SystemExit as exc:
            exit_code = exc.code if isinstance(exc.code, int) else 1
            if exit_code != 0:
                return ResultInfo(
                    name=name,
                    status=ResultStats.ERROR,
                    message=f"exit code {exit_code}",
                    elapsed_s=time.perf_counter() - start,
                )

        # Crash
        except Exception as exc:
            return ResultInfo(
                name=name,
                status=ResultStats.ERROR,
                message=str(exc) or repr(exc),
                elapsed_s=time.perf_counter() - start,
            )


    # Run file
    try:
        proc = subprocess.run(
            [str(file_runnable)],
            capture_output=True,
            text=True,
            cwd=str(input_path.parent),
            timeout=30,
            check=False,
        )

    # Can't run program
    except OSError as exc:
        return ResultInfo(
            name=name,
            status=ResultStats.ERROR,
            message=str(exc),
            elapsed_s=time.perf_counter() - start,
        )

    # Program crash
    if proc.returncode != 0:
        detail = proc.stderr.strip() or f"exit code {proc.returncode}"
        return ResultInfo(
            name=name,
            status=ResultStats.ERROR,
            message=detail,
            elapsed_s=time.perf_counter() - start,
        )

    # Check tests
    mismatches, n_tests = _parse_expectations(proc.stdout)
    if mismatches:
        details = ", ".join(f"'{exp}' != '{got}'" for exp, got in mismatches)
        return ResultInfo(
            name=name,
            status=ResultStats.FAILED,
            message=details,
            elapsed_s=time.perf_counter() - start,
        )

    # Ok
    return ResultInfo(
        name=name,
        status=ResultStats.OK,
        message=f"{n_tests}/{n_tests}",
        elapsed_s=time.perf_counter() - start,
    )


def _format_duration(seconds: float) -> str:
    if seconds < 1:
        return f"{seconds * 1000:.0f} ms"
    return f"{seconds:.2f} s"


def print_summary(results: list[ResultInfo]) -> None:
    """Print a colored summary table with timing benchmark."""
    if not results:
        return

    table = Table(title="Summary", show_lines=True)
    table.add_column("Example", style="cyan", no_wrap=True)
    table.add_column("Status", no_wrap=True)
    table.add_column("Duration", justify="right", style="magenta")
    table.add_column("Detail")

    passed = 0
    total_time = 0.0
    slowest = max(results, key=lambda r: r.elapsed_s)

    for result in results:
        total_time += result.elapsed_s
        if result.status == ResultStats.OK:
            passed += 1

        detail: str | Text = result.message
        if result.status != ResultStats.OK:
            detail = Text(result.message, style="red")

        table.add_row(
            result.name,
            Text(result.status.value, style=_STATUS_STYLES[result.status]),
            _format_duration(result.elapsed_s),
            detail,
        )

    console.print()
    console.print(table)

    failed = len(results) - passed
    summary_style = "bold green" if failed == 0 else "bold red"
    console.print(
        f"\n[bold]Benchmark[/bold]: "
        f"[{summary_style}]{passed}/{len(results)} passed[/] "
        f"— total [magenta]{_format_duration(total_time)}[/] "
        f"— slowest [yellow]{slowest.name}[/] "
        f"([magenta]{_format_duration(slowest.elapsed_s)}[/])"
    )


def run_all_examples(project_root: Path | None = None) -> list[ResultInfo]:
    """Run all examples and print the summary."""
    root = (project_root or Path(__file__).resolve().parents[1]).resolve()
    paths = discover_examples(root)

    console.print(
        f"[bold]Running {len(paths)} examples[/] from [cyan]{root / 'examples'}[/]\n"
    )

    results: list[ResultInfo] = []
    for path in paths:
        console.print("Testing [cyan]{:.<40}".format(path.parent.name + "[/]"), end=" ")
        infos = run_example(path, root)

        if infos.status == ResultStats.OK:
            console.print(infos.message)
        else:
            console.print("")

        results.append(infos)

    print_summary(results)
    return results


if __name__ == "__main__":
    results = run_all_examples()
    failed = [r for r in results if r.status != ResultStats.OK]
    sys.exit(1 if failed else 0)
