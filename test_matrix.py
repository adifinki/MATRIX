# to run pytest with description, run: `pytest -v -s test_matrix.py` in the terminal
import pytest as pytest

from main import Matrix


def test_matrix_str():
    m = Matrix(((1, 2), (3, 4)))
    assert str(m) == '((1, 2), (3, 4))'


def test_matrix_repr():
    m = Matrix(((1, 2), (3, 4)))
    assert repr(m) == 'Matrix(((1, 2), (3, 4)))'


def test_matrix_tuples():
    m = Matrix(((1, 2), (3, 4)))
    assert m.tuples == ((1, 2), (3, 4))


def test_matrix_shape():
    m = Matrix(((1, 2, 3), (3, 4, 5)))
    assert m.shape == (2, 3)


def test_matrix_addition():
    m = Matrix(((1, 2), (3, 4)))
    n = Matrix(((1, 2), (3, 4)))
    assert m + n == Matrix(((2, 4), (6, 8)))


def test_input_validation_addition():
    m = Matrix(((1, 2), (3, 4)))
    with pytest.raises(TypeError, match='Can not add Matrix with int'):
        m + 24  # type: ignore
    with pytest.raises(ValueError, match='Can not add matrices with different shape'):
        m + Matrix(((1, 2, 3), (3, 4, 5)))


def test_matrix_subtraction():
    m = Matrix(((1, 2), (3, 4)))
    n = Matrix(((1, 2), (3, 4)))
    assert m - n == Matrix(((0, 0), (0, 0)))


def test_input_validation_subtraction():
    m = Matrix(((1, 2), (3, 4)))
    with pytest.raises(TypeError, match='Can not sub Matrix with int'):
        m - 24  # type: ignore
    with pytest.raises(ValueError, match='Can not sub matrices with different shape'):
        m - Matrix(((1, 2, 3), (3, 4, 5)))


def test_valid_matrix_mult_shape():
    m = Matrix(((1, 2), (3, 4)))
    n = Matrix(((1, 2, 3), (3, 4, 5)))
    with pytest.raises(ValueError, match='Can not multiply matrices with difference shape'):
        m * n


def test_matrix_mult():
    m = Matrix(((1, 2), (3, 4)))
    n = Matrix.unity(2)
    assert m * n == m


def test_input_validation_mul():
    m = Matrix(((1, 2), (3, 4)))
    with pytest.raises(TypeError, match='Can not multiply Matrix with str'):
        m * 'a'  # type: ignore


def test_div():
    m = Matrix(((1, 2), (3, 4)))
    assert m/2 == Matrix(((0.5, 1), (1.5, 2)))


def test_eq():
    m = Matrix(((1, 2), (3, 4)))
    assert m == Matrix(((1, 2), (3, 4)))


def test_nq():
    m = Matrix(((1, 2), (3, 4)))
    assert m != Matrix(((1, 5), (3, 4)))


def test_unity():
    m = Matrix.unity(2)
    assert m == Matrix(((1, 0), (0, 1)))


def test_ones():
    m = Matrix.ones(2)
    assert m == Matrix(((1, 1), (1, 1)))






