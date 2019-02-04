def palindrome(string: str) -> str:
    # return ''.join(list(string)[::-1]) == string
    return all([val == string[len(string) - idx -1] for idx, val in enumerate(string)])

print(palindrome('hello'))
print(palindrome('abba'))
