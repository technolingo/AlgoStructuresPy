from .index import max_char


def test_max_char():
    assert max_char('Hello World') == 'l'
    assert max_char('a') == 'a'
    assert max_char('') == ''
    assert max_char('abcdefghijklmnaaaaa') == 'a'
    assert max_char('ab1c1d1e1f1g1') == '1'
