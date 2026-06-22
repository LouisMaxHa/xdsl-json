define i32 @somme_boucle() {
entry:
  %sum = alloca i32, align 4
  %i   = alloca i32, align 4
  store i32 0, ptr %sum, align 4  ; somme = 0
  store i32 0, ptr %i,   align 4  ; i = 0
  br label %loop_cond              ; goto boucle

loop_cond:                                 ; condition
  %i_cur = load i32, ptr %i,   align 4     ; charge i
  %cond  = icmp slt i32 %i_cur, 10         ; i < n ? (n = 10, connu à la compilation)
  br i1 %cond, label %loop_body, label %loop_end

loop_body:
  %i_body  = load i32, ptr %i,   align 4       ; charge i
  %sum_old = load i32, ptr %sum, align 4       ; charge acc
  %sum_new = add nsw i32 %sum_old, %i_body     ; acc = acc + i
  store i32 %sum_new, ptr %sum, align 4        ; stocke acc
  %i_next  = add nsw i32 %i_body, 1            ; i++
  store i32 %i_next, ptr %i, align 4
  br label %loop_cond

loop_end:
  %result = load i32, ptr %sum, align 4
  ret i32 %result
}
