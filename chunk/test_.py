from .index import chunk


def test_chunk():
    lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    assert chunk([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == lst
    assert chunk([], 2) == []
    assert chunk([1, 2, 3], 4) == [1, 2, 3]
    assert chunk([1, 2, 3], 0) == [1, 2, 3]
