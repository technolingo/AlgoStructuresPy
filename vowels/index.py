import re


def vowels(string: str) -> int:
    pattern = re.compile(r'[aeiou]', re.I)
    return len(re.findall(pattern, string))
