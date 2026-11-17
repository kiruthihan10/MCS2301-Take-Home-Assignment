"""MiniLang command-line entry point.

    python minilang.py run FILE --scope=static
    python minilang.py run FILE --scope=dynamic
    python minilang.py ast FILE
    python minilang.py check FILE
"""
import sys

from minilang_kit.errors import MiniLangError
from minilang_kit.interpreter import evaluate, format_value
from minilang_kit.parser import parse
from minilang_kit.typechecker import check

USAGE = ("usage: python minilang.py (run FILE --scope=static|dynamic"
         " | ast FILE | check FILE)")


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[0] not in ("run", "ast", "check"):
        print(USAGE)
        return 2
    command, path = argv[0], argv[1]
    scope = "static"
    for arg in argv[2:]:
        if arg.startswith("--scope="):
            scope = arg.split("=", 1)[1]
    if scope not in ("static", "dynamic"):
        print(USAGE)
        return 2
    with open(path, encoding="utf-8") as f:
        source = f.read()
    try:
        tree = parse(source)
        if command == "ast":
            print(tree.sexp())
        elif command == "check":
            check(tree)
            print("OK")
        else:
            check(tree)
            print(format_value(evaluate(tree, {}, scope)))
    except MiniLangError as e:
        print(e)
        return 1
    except NotImplementedError as e:
        print(f"NOT IMPLEMENTED: {e}")
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
