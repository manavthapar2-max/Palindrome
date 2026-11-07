def is_palindrome(value):
    if not isinstance(value, str):
        raise ValueError("Input must be a string")

    if len(value) == 1:
        return True

    return False