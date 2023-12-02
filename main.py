import operator
from typing import Callable

Self = 'Matrix'


# Purpose: Create a class to represent a two-dimensional array
class Matrix:
    """A class to represent a two-dimensional array"""

    def __init__(self, matrix: tuple[tuple[float, ...], ...]):
        self._matrix = matrix

    def __str__(self):
        """Return a string of the Matrix tuples.

        >>> str(Matrix(((1, 2), (3, 4))))
        '((1, 2), (3, 4))'
        """
        return str(self._matrix)

    def __repr__(self):
        """Return a string representation.

        >>> repr(Matrix(((1, 2), (3, 4))))
        'Matrix(((1, 2), (3, 4)))'
        """
        return f'{self.__class__.__name__}({self._matrix})'

    @property
    def tuples(self) -> tuple[tuple[float, ...], ...]:
        """Return the matrix tuples.

        >>> Matrix(((1, 2), (3, 4))).tuples
        ((1, 2), (3, 4))
        """
        return self._matrix

    @property
    def shape(self) -> tuple[int, int]:
        """Return the matrix shape.

        >>> Matrix(((1, 2), (3, 4))).shape
        (2, 2)
        """
        return len(self._matrix), len(self._matrix[0])

    def _activate_matrix_action(self, other: Self, action: Callable[[float, float], float]) -> Self:
        """Return the addition or subtraction of two matrices"""
        if not isinstance(other, self.__class__):
            raise TypeError(f"Can not {action.__name__} {self.__class__.__name__} with {type(other).__name__}")
        if self.shape != other.shape:
            raise ValueError(f"Can not {action.__name__} matrices with different shape")
        return self.__class__(
            tuple(tuple(action(n, m) for n, m in zip(row1, row2)) for row1, row2 in zip(self._matrix, other._matrix)))

    def __add__(self, other: Self) -> Self:
        """Return a new matrix, where each cell is the sum of the corresponding cells in self and other

        >>> Matrix(((1, 2), (3, 4))) + Matrix(((2, 3), (4, 5)))
        Matrix(((3, 5), (7, 9)))

        >>> Matrix(((1, 2), (3, 4))) + 4  # type: ignore
        Traceback (most recent call last):
        TypeError: Can not add Matrix with int

        >>> Matrix(((1, 2), (3, 4))) + Matrix(((1, 2, 3), (3, 4, 5)))
        Traceback (most recent call last):
        ValueError: Can not add matrices with different shape
        """
        return self._activate_matrix_action(other, operator.add)

    def __sub__(self, other: Self) -> Self:
        """Return a new matrix, where each cell is the sub of the corresponding cells in self and other

        >>> Matrix(((2, 3), (4, 5))) - Matrix(((1, 2), (3, 4)))
        Matrix(((1, 1), (1, 1)))

        >>> Matrix(((1, 2), (3, 4))) - 4  # type: ignore
        Traceback (most recent call last):
        TypeError: Can not sub Matrix with int

        >>> Matrix(((1, 2, 3), (3, 4, 5))) - Matrix(((1, 2), (3, 4)))
        Traceback (most recent call last):
        ValueError: Can not sub matrices with different shape
        """
        return self._activate_matrix_action(other, operator.sub)

    def _matrix_multiplication(self, other: Self) -> Self:
        """Return the multiplication of two matrices """
        if self.shape != other.shape[::-1]:
            raise ValueError('Can not multiply matrices with difference shape')
        return self.__class__(
            tuple(tuple(sum(n * m for n, m in zip(row, col)) for col in zip(*other._matrix)) for row in self._matrix))

    def __mul__(self, other) -> Self:
        """Return the multiplication of the matrix by scalar

        >>> Matrix(((2, 3), (4, 5))) * Matrix(((1, 2), (3, 4)))
        Matrix(((11, 16), (19, 28)))

        >>> Matrix(((2, 3), (4, 5))) * Matrix.unity(2)
        Matrix(((2, 3), (4, 5)))

        >>> Matrix(((1, 2), (3, 4))) * 4
        Matrix(((4, 8), (12, 16)))

        >>> Matrix(((1, 2), (3, 4))) * '4'  # type: ignore
        Traceback (most recent call last):
        TypeError: Can not multiply Matrix with str

        >>> Matrix(((1, 2, 3), (3, 4, 5))) * Matrix(((1, 2), (3, 4)))
        Traceback (most recent call last):
        ValueError: Can not multiply matrices with difference shape
        """
        if type(other) in (int, float):
            return self * self.unity(self.shape[0], value=other)
        if isinstance(other, self.__class__):
            return self._matrix_multiplication(other)
        raise TypeError(f"Can not multiply {self.__class__.__name__} with {type(other).__name__}")

    def __rmul__(self, other) -> Self:
        """Return the multiplication of the matrix by scalar"""
        return self * other

    def __truediv__(self, scalar: float) -> Self:
        """Return the division of the matrix by scalar"""
        return self * (1 / scalar)

    def __eq__(self, other: Self) -> bool:
        """Return True if two matrices are equal

        >>> Matrix(((1, 2), (3, 4))) == Matrix(((1, 2), (3, 4)))
        True

        >>> Matrix(((1, 2), (3, 4))) == Matrix(((1, 1), (4, 4)))
        False
        """
        return self.tuples == other.tuples

    def __ne__(self, other):
        """Return True if two matrices are not equal"""
        return not self == other

    @classmethod
    def unity(cls, n: int, value: int | float | None = 1) -> Self:
        """Return the unity matrix of size n
        if value is given, returns value * the unity matrix

        >>> Matrix.unity(3)
        Matrix(((1, 0, 0), (0, 1, 0), (0, 0, 1)))

        >>> Matrix.unity(3, value=2)
        Matrix(((2, 0, 0), (0, 2, 0), (0, 0, 2)))
        """
        return cls(tuple(tuple(value * int(i == j) for i in range(n)) for j in range(n)))

    @classmethod
    def ones(cls, n: int) -> Self:
        """Return the ones matrix of size n

        >>> Matrix.ones(3)
        Matrix(((1, 1, 1), (1, 1, 1), (1, 1, 1)))
        """
        return cls(((1, ) * n, ) * n)

    def __hash__(self):
        """Return a hash value for matrix

        >>> hash(Matrix.unity(2))
        -641825214948741500
        """
        return hash(self._matrix)
