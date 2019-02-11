def pyramid(n):
    if n <= 0:
        print('Input must be greater than zero.')
    else:
        for i in range(1, n + 1):
            side = n - i
            centre = i * 2 - 1
            print(' ' * side + '#' * centre + ' ' * side)
