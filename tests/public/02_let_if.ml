# let, if, comparison and boolean operators
# expect ast: (let x 5 (if (and (< x 10) (not (== x 3))) (* x 2) 0))
# expect check: OK
# expect static: 10
# expect dynamic: 10
let x = 5 in
if x < 10 and not (x == 3) then x * 2 else 0
