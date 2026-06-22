module {
  func.func @somme_boucle() -> i32 {
    %n   = arith.constant 10 : index // n = 10 (connu à la compilation)
    %sum = arith.constant 0 : i32      // somme = 0
    %c0  = arith.constant 0 : index
    %c1  = arith.constant 1 : index

    %somme = scf.for %i = %c0 to %n step %c1
        iter_args(%acc = %sum) -> i32 {
      %i_i32 = arith.index_cast %i : index to i32 // cast i en i32
      %add   = arith.addi %acc, %i_i32 : i32      // acc = acc + i
      scf.yield %add : i32                        // itération suivante
    }

    return %somme : i32
  }
}
