from .index import steps


def test_steps_success(capsys):
    expected = '#    \n##   \n###  \n#### \n#####\n'
    steps(5)
    out, err = capsys.readouterr()
    assert out == expected


def test_steps_fail(capsys):
    error = 'Input must be greater than zero.\n'
    steps(-5)
    out, err = capsys.readouterr()
    assert out == error
