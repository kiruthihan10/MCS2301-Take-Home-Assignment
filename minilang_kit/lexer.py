"""Lexer for MiniLang.

Turns source text into a list of Token objects, each with a 1-based line and
column so the parser can report errors as
    PARSE ERROR at <line>:<col>: expected <token>

Comments start with '#' and run to the end of the line (use them for the
expected output in your test programs).

The lexer recognises the tokens of every variant (% <= != , and the minus
sign). Words such as 'xor' and 'max' are returned as IDENT tokens; if your
variant needs one of them as a keyword, add it to VARIANT_KEYWORDS.
"""
import string
from dataclasses import dataclass

from .errors import ParseError

KEYWORDS = {"let", "in", "fun", "if", "then", "else", "true", "false",
            "and", "or", "not"}

# Add 'xor' (variant 3/8) or 'max' (variant 2/7) here if you need it.
VARIANT_KEYWORDS: set[str] = set()

# Longest operators first, so '<=' is not read as '<' followed by '='.
# Identifiers and numbers use ASCII only, the same as the Java kit.
DIGITS = set(string.digits)
LETTERS = set(string.ascii_letters)

OPERATORS = ["<=", "==", "!=", "+", "-", "*", "/", "^", "%", "<", "=",
             "(", ")", ","]


@dataclass
class Token:
    kind: str   # 'INT', 'IDENT', 'KEYWORD', 'OP' or 'EOF'
    value: str  # the text of the token ('' for EOF)
    line: int
    col: int

    def __repr__(self) -> str:
        return f"Token({self.kind}, {self.value!r}, {self.line}:{self.col})"


def tokenize(source: str) -> list[Token]:
    tokens: list[Token] = []
    i, line, col = 0, 1, 1
    n = len(source)
    while i < n:
        ch = source[i]
        if ch == "\n":
            i, line, col = i + 1, line + 1, 1
            continue
        if ch in " \t\r":
            i, col = i + 1, col + 1
            continue
        if ch == "#":                      # comment to end of line
            while i < n and source[i] != "\n":
                i += 1
            continue
        start_col = col
        if ch in DIGITS:
            j = i
            while j < n and source[j] in DIGITS:
                j += 1
            tokens.append(Token("INT", source[i:j], line, start_col))
            col += j - i
            i = j
            continue
        if ch in LETTERS:
            j = i
            while j < n and (source[j] in LETTERS or source[j] in DIGITS
                             or source[j] == "_"):
                j += 1
            word = source[i:j]
            kind = "KEYWORD" if word in KEYWORDS | VARIANT_KEYWORDS else "IDENT"
            tokens.append(Token(kind, word, line, start_col))
            col += j - i
            i = j
            continue
        for op in OPERATORS:
            if source.startswith(op, i):
                tokens.append(Token("OP", op, line, start_col))
                i, col = i + len(op), col + len(op)
                break
        else:
            raise ParseError(line, col, f"a valid token, found '{ch}'")
    tokens.append(Token("EOF", "", line, col))
    return tokens
