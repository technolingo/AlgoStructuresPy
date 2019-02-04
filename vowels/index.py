import re


def vowels(string: str) -> int:
    pattern = re.compile(r'[aeiou]', re.I)
    return len(re.findall(pattern, string))

print(vowels('hello world!'))
print(vowels('h'))
print(vowels('haaa'))
