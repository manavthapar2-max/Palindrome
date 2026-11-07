from collections import deque


def is_palindrome(value):
    if not isinstance(value, str):
        raise ValueError("Input must be a string")

    if not value:
        return False

    characters = deque(value)

    while len(characters) > 1:
        if characters.popleft() != characters.pop():
            return False

    return True