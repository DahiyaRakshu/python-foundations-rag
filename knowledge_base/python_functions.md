# Python fundamentals: functions and practical structure

A function packages reusable instructions. Define one with `def`, a name, parentheses, and an indented body. For example:

    def greet(name):
        return "Hello, " + name

Call it with `greet("Sam")`. Parameters are names in the definition; arguments are the values supplied in a call. `return` sends a result back to the caller. If a function reaches its end without a return statement, it returns `None`. A default parameter value can make an argument optional.

Functions can process collections. For example, a loop can visit each name in a list and call a function for each one. Keep a function focused on one task, and choose descriptive names. A docstring is a string at the start of a function body that documents its purpose.

Use `try` and `except` to handle an error that you know how to recover from. For example, convert text to an integer inside `try` and catch `ValueError` if the text is not a valid integer. Avoid catching every error without a reason; unexpected errors can signal a bug.

Modules are Python files that can be imported. `import math` makes the module available under its name; `from math import sqrt` imports one named item. The standard library includes modules for common tasks. A script can place code that should run only when executed directly under `if __name__ == "__main__":`.

A dictionary stores key-value pairs. Square-bracket lookup such as `scores["Mina"]` raises `KeyError` if the key is absent. The `.get("Mina")` method returns `None` for a missing key by default, or a supplied fallback such as `.get("Mina", 0)`. This is useful when processing names that may not all appear in a mapping.

This guide is an introductory summary and does not document the complete Python language reference.
