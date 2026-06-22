from __future__ import annotations

from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Sequence
from enum import EnumMeta

from pydantic import BaseModel, ConfigDict
from xdsl.builder import Builder

from xdsljson.variables.val.val import ValNode


# ABC : Abstract Base Class
class OpNode(BaseModel, ABC):
    # Necessaire pour autoriser les classes externes (xDSL: Builder)
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __repr__(self) -> str:
        return type(self).__name__

    # Force les sous-classes à implémenter cette méthode abstraite
    @abstractmethod
    def codegen(self, builder: Builder) -> Sequence[ValNode]:
        """Génère l'opération xDSL et retourne la SSA produite."""
        raise NotImplementedError

class ABCEnumMeta(EnumMeta, ABCMeta):
    """Permet d'hériter à la fois de Enum et de ValNode (ABC)."""
