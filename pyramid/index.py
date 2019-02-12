'''
Write a function that accepts a positive number N.
The function should console log a pyramid shape
with N levels using the # character.  Make sure the
pyramid has spaces on both the left *and* right hand sides
--- Examples
  pyramid(1)
      '#'
  pyramid(2)
      ' # '
      '###'
  pyramid(3)
      '  #  '
      ' ### '
      '#####'

pattern analysis
      '  #  '
      ' ### '
      '#####'
     '#######'
    '#########'
   '###########'
if we count from 1
n: 1, 2, 3, 4, 5, 6, 7
l: 1, 3, 5, 7, 9, 11, 13
length is n * 2 - 1, always odd
each side is n - i, centre is i * 2 - 1
'''


def pyramid(n):
    if n <= 0:
        print('Input must be greater than zero.')
    else:
        for i in range(1, n + 1):
            side = n - i
            centre = i * 2 - 1
            print(' ' * side + '#' * centre + ' ' * side)
