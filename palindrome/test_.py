from .index import is_palindrome


def test_is_palindrome():
    assert is_palindrome('heLLo') is False
    assert is_palindrome('abba') is True
    assert is_palindrome('A') is True
    assert is_palindrome('') is True
