from .index import pyramid


def test_pyramid_success(capsys):
    expected = '    #    \n   ###   \n  #####  \n ####### \n#########\n'
    pyramid(5)
    out, err = capsys.readouterr()
    assert out == expected


def test_pyramid_fail(capsys):
    error = 'Input must be greater than zero.\n'
    pyramid(-5)
    out, err = capsys.readouterr()
    assert out == error
