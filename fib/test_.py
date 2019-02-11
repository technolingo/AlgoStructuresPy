from .index import fib


def test_fib():
    assert fib(0, foo='hello') == 0
    assert fib(1, foo='hello', bar='world') == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(6) == 8
