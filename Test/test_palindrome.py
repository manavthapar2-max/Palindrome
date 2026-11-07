import pytest
from palindrome import is_palindrome


def test_invalid_input():
    with pytest.raises(ValueError):
        is_palindrome(123)