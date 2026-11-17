"""AST node classes for MiniLang.

Every node has sexp(), which returns the S-expression required by the
`ast` command, for example (+ 1 2) or (let x e1 e2).
You may add fields (for example a source position) or extra node types.
"""
from dataclasses import dataclass


class Node:
    def sexp(self) -> str:
        raise NotImplementedError


@dataclass
class Num(Node):
    value: int

    def sexp(self) -> str:
        return str(self.value)


@dataclass
class Bool(Node):
    value: bool

    def sexp(self) -> str:
        return "true" if self.value else "false"


@dataclass
class Var(Node):
    name: str

    def sexp(self) -> str:
        return self.name


@dataclass
class BinOp(Node):
    """Binary operator: + - * / ^ < == and or, plus your variant's operator."""
    op: str
    left: Node
    right: Node

    def sexp(self) -> str:
        return f"({self.op} {self.left.sexp()} {self.right.sexp()})"


@dataclass
class Not(Node):
    expr: Node

    def sexp(self) -> str:
        return f"(not {self.expr.sexp()})"


@dataclass
class Let(Node):
    name: str
    value: Node
    body: Node

    def sexp(self) -> str:
        return f"(let {self.name} {self.value.sexp()} {self.body.sexp()})"


@dataclass
class If(Node):
    cond: Node
    then_branch: Node
    else_branch: Node

    def sexp(self) -> str:
        return (f"(if {self.cond.sexp()} {self.then_branch.sexp()} "
                f"{self.else_branch.sexp()})")


@dataclass
class FunDef(Node):
    """let fun name(param) = body in rest"""
    name: str
    param: str
    body: Node
    rest: Node

    def sexp(self) -> str:
        return (f"(fun {self.name} {self.param} {self.body.sexp()} "
                f"{self.rest.sexp()})")


@dataclass
class Call(Node):
    name: str
    arg: Node

    def sexp(self) -> str:
        return f"(call {self.name} {self.arg.sexp()})"


# ---- Variant nodes (use the ones for your two constructs) ----

@dataclass
class Neg(Node):
    """Unary minus, variant 0/5."""
    expr: Node

    def sexp(self) -> str:
        return f"(neg {self.expr.sexp()})"


@dataclass
class Max(Node):
    """Built-in max(a, b), variant 2/7."""
    left: Node
    right: Node

    def sexp(self) -> str:
        return f"(max {self.left.sexp()} {self.right.sexp()})"

# Variants 1/6 (%), 3/8 (xor) and 4/9 (<=, !=) use BinOp.
