def pyramid(n):
    for i in range(1, n + 1):
        side = n - i
        centre = i * 2 - 1
        print(' ' * side + '#' * centre + ' ' * side)

pyramid(5)
