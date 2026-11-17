# MiniLang starter kit (Python)

MCS2301 Principles of Programming Languages. Python 3.10 or later, standard library only.

## What is provided

| File | Contents |
|---|---|
| `minilang.py` | Command-line entry point (`run`, `ast`, `check`), already in the required format |
| `minilang_kit/lexer.py` | Complete lexer with line:column positions and `#` comments |
| `minilang_kit/ast_nodes.py` | AST node classes; `sexp()` prints the required S-expression |
| `minilang_kit/errors.py` | `ParseError`, `TypeCheckError`, `RuntimeErrorML`, which print the required one-line messages |
| `minilang_kit/parser.py` | Parser skeleton with token helpers (`peek`, `match`, `expect`); **you write the grammar methods** |
| `minilang_kit/typechecker.py` | **To be written** (Task 3) |
| `minilang_kit/interpreter.py` | **To be written** (Task 4) |
| `run_tests.py` | Test runner; also writes `results.txt` |
| `tests/public/` | The five public test programs |

You may extend or replace any of these files.

## Commands

    python minilang.py ast FILE
    python minilang.py check FILE
    python minilang.py run FILE --scope=static
    python minilang.py run FILE --scope=dynamic

Until you implement a part, the command prints `NOT IMPLEMENTED: ...`.

## Writing test programs

Put the expected output in comments at the top of each `.ml` file, one line per command:

    # expect ast: (+ 1 (* 2 3))
    # expect check: OK
    # expect static: 7
    # expect dynamic: 7
    1 + 2 * 3

Keys are `ast`, `check`, `static` and `dynamic`. For errors, the expected text only has to be the start of the output, so `# expect check: TYPE ERROR` accepts any type-error message, and `# expect ast: PARSE ERROR at 3:11` accepts any wording of the expected token. Comment lines count when line numbers are reported.

## Running the tests

    python run_tests.py                 # every .ml file under tests/
    python run_tests.py tests/public    # one folder only

The runner prints PASS or FAIL for each expectation and writes every command and its actual output to `results.txt`, which you submit in your repository.

## Variant notes

Your group implements two extra constructs (A from d1, B from d2; see the assignment sheet). The lexer already produces the tokens for every variant (`%`, `<=`, `!=`, `,` and `-`). The words `xor` and `max` come out as `IDENT` tokens; add the one you need to `VARIANT_KEYWORDS` in `lexer.py` if you want it treated as a keyword. `Neg` and `Max` nodes are provided for variants 0/5 and 2/7; the other variants use `BinOp`.
