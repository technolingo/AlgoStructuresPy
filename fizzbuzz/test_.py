from .index import fizzbuzz


def test_fizzbuzz_success(capsys):
    fizzbuzz(16)
    out, err = capsys.readouterr()
    s = "1\n2\nfizz\n4\nbuzz\nfizz\n7\n8\nfizz\nbuzz\n11\nfizz\n13\n14\nfizzbuzz\n16\n"  # noqa
    assert out == s


def test_fizzbuzz_fail(capsys):
    error = 'Input must be greater than zero.\n'
    fizzbuzz(-5)
    out, err = capsys.readouterr()
    assert out == error
