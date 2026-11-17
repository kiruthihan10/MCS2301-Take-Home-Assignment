# Static vs dynamic scoping (the example in the assignment brief)
# expect ast: (let rate 3 (fun scale n (* n rate) (let rate 10 (if (and (< (call scale 2) 10) (not (== rate 0))) (+ (call scale 2) 1) 0))))
# expect check: OK
# expect static: 7
# expect dynamic: 0
let rate = 3 in
let fun scale(n) = n * rate in
let rate = 10 in
if scale(2) < 10 and not (rate == 0)
then scale(2) + 1
else 0
