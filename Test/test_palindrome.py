import pytest
from palindrome import is_palindrome


def test_invalid_input():
    with pytest.raises(ValueError):
        is_palindrome(123)

def test_empty_string():
    assert is_palindrome("") is False

def test_single_character():
    assert is_palindrome("a") is True