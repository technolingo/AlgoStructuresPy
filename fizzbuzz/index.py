from typing import overload


@overload
def fizzbuzz(n:int) -> int:
    ...

@overload
def fizzbuzz(n:int) -> str:
    ...

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)

fizzbuzz(20)
