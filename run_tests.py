"""MiniLang test runner (works for Python and Java submissions).

Each test program states its expected outputs in comments, one per line:

    # expect ast: (+ 1 (* 2 3))
    # expect check: OK
    # expect static: 7
    # expect dynamic: 7

Keys: ast, check, static (run --scope=static), dynamic (run --scope=dynamic).
For errors, the expected text only needs to be a prefix of the actual output,
so "# expect check: TYPE ERROR" accepts any type-error message and
"# expect ast: PARSE ERROR at 1:11" accepts any expected-token wording.

Usage:
    python run_tests.py                       # runs every .ml file under tests/
    python run_tests.py --cmd "java -jar minilang.jar"
    python run_tests.py tests/public tests/mine --out results.txt
"""
import argparse
import glob
import os
import shlex
import subprocess
import sys

KEY_ARGS = {
    "ast": ["ast"],
    "check": ["check"],
    "static": ["run", "--scope=static"],
    "dynamic": ["run", "--scope=dynamic"],
}
ERROR_PREFIXES = ("PARSE ERROR", "TYPE ERROR", "RUNTIME ERROR")


def expectations(path):
    found = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s.startswith("#") and "expect" in s:
                body = s.lstrip("#").strip()
                if body.startswith("expect ") and ":" in body:
                    key, value = body[len("expect "):].split(":", 1)
                    key = key.strip()
                    if key in KEY_ARGS:
                        found.append((key, value.strip()))
    return found


def matches(expected, actual):
    if expected.startswith(ERROR_PREFIXES):
        return actual.startswith(expected)
    return actual == expected


def run(cmd, key, path):
    args = shlex.split(cmd)
    sub = KEY_ARGS[key]
    full = args + [sub[0], path] + sub[1:]
    try:
        out = subprocess.run(full, capture_output=True, text=True, timeout=10)
        text = (out.stdout or "").strip().splitlines()
        return " ".join(full), (text[0] if text else (out.stderr or "").strip())
    except subprocess.TimeoutExpired:
        return " ".join(full), "TIMEOUT"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dirs", nargs="*", default=["tests"])
    ap.add_argument("--cmd", default=None,
                    help='command to run MiniLang (default: "python minilang.py",'
                         ' or "java -jar minilang.jar" if minilang.py is absent)')
    ap.add_argument("--out", default="results.txt")
    a = ap.parse_args()
    if a.cmd is None:
        a.cmd = (f"{shlex.quote(sys.executable)} minilang.py" if os.path.exists("minilang.py")
                 else "java -jar minilang.jar")

    files = []
    for d in a.dirs:
        files += sorted(glob.glob(os.path.join(d, "**", "*.ml"), recursive=True))
    if not files:
        print("no .ml files found")
        return 1

    passed = total = skipped = 0
    lines = []
    for path in files:
        exps = expectations(path)
        if not exps:
            print(f"SKIP {path} (no '# expect' lines)")
            skipped += 1
            continue
        with open(path, encoding="utf-8") as f:
            lines += [f"=== {path}", f.read().rstrip(), ""]
        for key, expected in exps:
            total += 1
            command, actual = run(a.cmd, key, path)
            ok = matches(expected, actual)
            passed += ok
            status = "PASS" if ok else "FAIL"
            print(f"{status} {path} [{key}]" + ("" if ok else
                  f"\n     expected: {expected}\n     actual:   {actual}"))
            lines += [f"$ {command}", actual, f"[{status}] expected: {expected}", ""]
    summary = f"{passed}/{total} passed" + (f", {skipped} file(s) skipped (no '# expect' lines)" if skipped else "")
    print("\n" + summary)
    if total == 0:
        print("FAIL: no expectations were checked")
    with open(a.out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + f"\n{summary}\n")
    print(f"results written to {a.out}")
    return 0 if total > 0 and passed == total and skipped == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
