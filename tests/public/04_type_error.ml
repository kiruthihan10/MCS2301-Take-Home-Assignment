# Branches of an if have different types
# expect ast: (if (< 1 2) 3 false)
# expect check: TYPE ERROR
if 1 < 2 then 3 else false
