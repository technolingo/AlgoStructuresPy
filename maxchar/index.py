def maxChar(string:str) -> str:
    ''' Return the most frequent character in a string.'''
    charMap = {}

    for char in string:
        if char in charMap:
            charMap[char] += 1 or 1
        else:
            charMap[char] = 1

    return max([(val, char) for char, val in charMap.items()])[1]

print(maxChar('Hello World'))
print(maxChar('a'))
print(maxChar('abcdefghijklmnaaaaa'))
print(maxChar('ab1c1d1e1f1g1'))
