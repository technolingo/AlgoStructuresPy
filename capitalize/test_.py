from .index import capitalize


def test_capitalize():
    assert capitalize('hello world!') == 'Hello World!'
