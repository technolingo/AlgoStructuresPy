def anagrams(string_a: str, string_b: str) -> bool:
    first = ''.join(sorted(list(string_a.replace(r'[^a-zA-Z]', ''))))
    second = ''.join(sorted(list(string_b.replace(r'[^a-zA-Z]', ''))))
    return first == second

print(anagrams('hello', 'llohe')) # True
print(anagrams('Whoa! Hi!', 'Hi! Whoa!')) # True
print(anagrams('One One', 'Two two two')) # False
print(anagrams('One one', 'One one c')) # False
print(anagrams('A tree, a life, a bench', 'A tree, a fence, a yard')) # False
