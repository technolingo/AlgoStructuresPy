def reverse_string(string: str) -> str:
    lst = list(string)
    lst.reverse()
    return string[::-1]

print(
    reverse_string('hello world')
)
