def fizzbuzz(n: int):
    if n <= 0:
        print('Input must be greater than zero.')
    else:
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print('fizzbuzz')
            elif i % 3 == 0:
                print('fizz')
            elif i % 5 == 0:
                print('buzz')
            else:
                print(i)
