"""Recursive-descent parser for MiniLang (Task 2) - TO BE WRITTEN.

The helper methods below handle the token stream and produce parse errors
in the required format. Write one parse_... method per nonterminal of your
grammar (grammar.ebnf), and rewrite left-recursive rules as loops
(left-associative) or right recursion (right-associative).
"""
from .ast_nodes import Node
from .errors import ParseError
from .lexer import Token, tokenize


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.pos = 0

    # ---- helpers ----

    def peek(self) -> Token:
        return self.tokens[self.pos]

    def advance(self) -> Token:
        tok = self.tokens[self.pos]
        if tok.kind != "EOF":
            self.pos += 1
        return tok

    def check(self, kind: str, value: str | None = None) -> bool:
        tok = self.peek()
        return tok.kind == kind and (value is None or tok.value == value)

    def match(self, kind: str, value: str | None = None) -> bool:
        """Consume the next token if it matches; return whether it did."""
        if self.check(kind, value):
            self.advance()
            return True
        return False

    def expect(self, kind: str, value: str | None = None) -> Token:
        """Consume the next token, or raise a parse error at its position."""
        if self.check(kind, value):
            return self.advance()
        tok = self.peek()
        wanted = value if value is not None else kind.lower()
        raise ParseError(tok.line, tok.col, wanted)

    # ---- grammar ----

    def parse_program(self) -> Node:
        node = self.parse_expr()
        self.expect("EOF")          # the whole input must be one expression
        return node

    def parse_expr(self) -> Node:
        # TODO: implement your grammar, starting from the lowest-precedence
        # level (let / if / fun, then or, and, not, comparison, ...).
        raise NotImplementedError("parser not implemented yet")


def parse(source: str) -> Node:
    return Parser(tokenize(source)).parse_program()
