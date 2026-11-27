# Python fundamentals: core concepts

Python programs store values in names called variables. Assignment uses `=`, as in `count = 3` or `language = "Python"`. Common built-in types include integers (`int`), decimal numbers (`float`), strings (`str`), and Boolean values (`bool`). Strings can be written with single or double quotes. Use `type(value)` to inspect a value's type.

Python uses indentation to mark blocks of code. An `if` statement runs a block when its condition is true; `elif` checks another condition and `else` handles the remaining case. Comparisons include `==`, `!=`, `<`, `<=`, `>`, and `>=`. The Boolean operators are `and`, `or`, and `not`.

A `for` loop visits items in an iterable. For example, `for name in names:` repeats once for each item in `names`. `range(5)` supplies the integer values 0, 1, 2, 3, and 4; the stop value is excluded. A `while` loop repeats while its condition remains true. Use `break` to exit a loop early and `continue` to skip to its next iteration.

A list is an ordered, mutable collection, written with square brackets, such as `colors = ["blue", "green"]`. Lists support indexing starting at zero, and `append` adds an item. A tuple is ordered but immutable, and is written with parentheses, such as `(10, 20)`. A dictionary maps unique keys to values, such as `person = {"name": "Ada"}`. Retrieve a value using `person["name"]`; use `person.get("age", 0)` when a default is useful. A set stores distinct values without promising sequence order.

This guide covers introductory language behavior, not every Python feature or version-specific change.
