from .index import vowels


def test_vowels():
    assert vowels('hello world!') == 3
    assert vowels('h') == 0
    assert vowels('haaaa') == 4
