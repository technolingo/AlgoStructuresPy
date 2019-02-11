from typing import Dict


def max_char(string: str) -> str:
    ''' Return the most frequent character in a string.'''
    if len(string) == 0:
        return ''

    char_map: Dict[str, int] = {}

    for char in string:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1

    return max([(val, char) for char, val in char_map.items()])[1]
