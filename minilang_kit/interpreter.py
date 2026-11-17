"""Interpreter for MiniLang (Task 4) - TO BE WRITTEN.

scope is 'static' or 'dynamic'. Raise RuntimeErrorML(message) for run-time
errors such as division by zero.

Integer division rounds toward zero, so (0 - 7) / 2 is -3. Python's // rounds
down (-7 // 2 is -4), so do not use it directly for negative operands.
A negative exponent in ^ is a run-time error.
"""
from .ast_nodes import Node
from .errors import RuntimeErrorML  # noqa: F401  (you will need it)


def evaluate(node: Node, env: dict, scope: str):
    # TODO: one case per node type. Under static scoping a function value
    # must remember its defining environment (a closure); under dynamic
    # scoping the body is evaluated in the environment at the call.
    raise NotImplementedError("interpreter not implemented yet")


def format_value(value) -> str:
    """Print values as required: 7, true or false."""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)
