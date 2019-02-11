def steps(n):
    if n <= 0:
        print('Input must be greater than zero.')
    else:
        for i in range(1, n + 1):
            print('#' * i + ' ' * (n - i))
