# Precedence of + - * / and a single ^
# expect ast: (- (+ 1 (* 2 (^ 3 2))) (/ 8 4))
# expect check: OK
# expect static: 17
# expect dynamic: 17
1 + 2 * 3 ^ 2 - 8 / 4
