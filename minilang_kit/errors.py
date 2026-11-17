"""Error types. Each one prints as exactly one line in the required format."""


class MiniLangError(Exception):
    """Base class for all MiniLang errors."""


class ParseError(MiniLangError):
    def __init__(self, line: int, col: int, expected: str):
        super().__init__(f"PARSE ERROR at {line}:{col}: expected {expected}")
        self.line, self.col, self.expected = line, col, expected


class TypeCheckError(MiniLangError):
    def __init__(self, message: str):
        super().__init__(f"TYPE ERROR: {message}")


class RuntimeErrorML(MiniLangError):
    def __init__(self, message: str):
        super().__init__(f"RUNTIME ERROR: {message}")
