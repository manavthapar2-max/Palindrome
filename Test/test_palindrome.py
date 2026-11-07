import pytest
from palindrome import is_palindrome


def test_invalid_input():
    with pytest.raises(ValueError):
        is_palindrome(123)

def test_empty_string():
    assert is_palindrome("") is False

def test_single_character():
    assert is_palindrome("a") is True

def test_two_same_characters():
    assert is_palindrome("bb") is True

def test_not_palindrome():
    assert is_palindrome("abc") is False

def test_laval_palindrome():
    assert is_palindrome("laval") is True

def test_toronto_not_palindrome():
    assert is_palindrome("toronto") is False

def test_sentence_palindrome():
    assert is_palindrome("Able was I ere I saw Elba") is True

