# Maps each closing bracket to the opening bracket it must match.
MATCHING_BRACKETS = {")": "(", "]": "[", "}": "{"}


def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.

    Approach: walk the string left to right using a list as a stack (LIFO).
    - Opening brackets are pushed onto the stack.
    - A closing bracket must match the most recently opened bracket, which is
      the top of the stack; if it doesn't (or the stack is empty), the string
      is unbalanced.
    - Any other characters are ignored.
    At the end, every opener must have been closed, so the stack must be empty.
    """
    stack = []
    openers = set(MATCHING_BRACKETS.values())

    for char in s:
        if char in openers:
            stack.append(char)
        elif char in MATCHING_BRACKETS:
            # A closer with nothing open, or closing the wrong type, is invalid.
            if not stack or stack.pop() != MATCHING_BRACKETS[char]:
                return False

    # Leftover openers mean something was never closed, e.g. "(()".
    return not stack
