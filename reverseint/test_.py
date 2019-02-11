from .index import reverse_int


def test_reverse_int():
    assert reverse_int(0) == 0
    assert reverse_int(34) == 43
    assert reverse_int(-46) == -64
