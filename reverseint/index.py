'''
Given an integer, return an integer that is the reverse
ordering of numbers.
--- Examples
  reverseInt(15) == 51
  reverseInt(981) == 189
  reverseInt(500) == 5
  reverseInt(-15) == -51
  reverseInt(-90) == -9
'''


def reverse_int(n):
    if n >= 0:
        return int(str(n)[::-1])
    return int(str(abs(n))[::-1]) * -1
