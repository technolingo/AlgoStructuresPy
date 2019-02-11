from .index import are_anagrams


def test_are_anagrams_true():
    assert are_anagrams('', '') is True
    assert are_anagrams('a', 'a') is True
    assert are_anagrams('hello', 'llohe') is True
    assert are_anagrams('Whoa! Hi!', 'Hi! Whoa!') is True


def test_are_anagrams_false():
    assert are_anagrams('One One', 'Two two two') is False
    assert are_anagrams('One one', 'One one c') is False
    assert are_anagrams('tree, bench', 'fence, yard') is False
