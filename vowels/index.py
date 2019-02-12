'''
Write a function that returns the number of vowels
used in a string.  Vowels: 'a', 'e', 'i', 'o', & 'u'.
--- Examples
  vowels('Hi There!') --> 3
  vowels('Why do you ask?') --> 4
  vowels('Why?') --> 0
'''
import re


def vowels(string: str) -> int:
    pattern = re.compile(r'[aeiou]', re.I)
    return len(re.findall(pattern, string))
