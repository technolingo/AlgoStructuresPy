'''
Given a string, return a new string with the reversed
order of characters
--- Examples
  reverse('apple') == 'leppa'
  reverse('hello') == 'olleh'
  reverse('Greetings!') == '!sgniteerG'
'''


def reverse_string(string: str) -> str:
    lst = list(string)
    lst.reverse()
    return string[::-1]
