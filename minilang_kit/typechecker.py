"""Type checker for MiniLang (Task 3) - TO BE WRITTEN.

Follow your attribute grammar: the environment `env` is the inherited
attribute (variable name -> type) and the returned type is the synthesised
attribute. Raise TypeCheckError(message) for type errors.
"""
from .ast_nodes import Node
from .errors import TypeCheckError  # noqa: F401  (you will need it)

INT, BOOL, FUN = "int", "bool", "int -> int"


def type_of(node: Node, env: dict[str, str]) -> str:
    # TODO: one case per node type
    raise NotImplementedError("type checker not implemented yet")


def check(node: Node) -> str:
    return type_of(node, {})
