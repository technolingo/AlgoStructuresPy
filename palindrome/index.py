'''
Given a string, return true if the string is a palindrome
or false if it is not.  Palindromes are strings that
form the same word if it is reversed. *Do* include spaces
and punctuation in determining if the string is a palindrome.
--- Examples:
  palindrome("abba") == true
  palindrome("abcdefg") == false
'''


def is_palindrome(string: str) -> str:
    # return ''.join(list(string)[::-1]) == string
    return all([val == string[len(string) - idx - 1] for idx, val in enumerate(string)])
