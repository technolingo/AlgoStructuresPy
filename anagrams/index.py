import re


def are_anagrams(string_a: str, string_b: str) -> bool:
    ''' Check to see if two provided strings are anagrams of eachother.
        One string is an anagram of another if it uses the same characters
        in the same quantity. Only consider characters, not spaces
        or punctuation.  Consider capital letters to be the same as lower case
    '''
    pattern = re.compile(r'[^a-z]')
    # convert to lowercase, remove non-alpha chars, sort both strings
    first = ''.join(sorted(list(pattern.sub('', string_a.lower()))))
    second = ''.join(sorted(list(pattern.sub('', string_b.lower()))))
    return first == second
