import operator
from typing import Callable
Self = 'Matrix'


# Purpose: Create a class to represent a two-dimensional array
class Matrix:
    """A class to represent a two-dimensional array"""
    def __init__(self, matrix: tuple[tuple[float, ...], ...]):
        self._matrix = matrix

    def __str__(self):
        """Return a string representation: ((1, 2), (3, 4))"""
        return str(self._matrix)

    def __repr__(self):
        """ return: a string representation: Matrix(((1, 2), (3, 4)))"""
        return f'Matrix({self._matrix})'

    @property
    def tuples(self):
        """Return the matrix"""
        return self._matrix

    def _addition_subtraction(self, other: Self, symbol: Callable[[float, float], float]) -> Self:
        """Return the addition or subtraction of two matrices"""
        return self.__class__(
            tuple(tuple(symbol(n, m) for n, m in zip(row1, row2)) for row1, row2 in zip(self._matrix, other._matrix)))

    def __add__(self, other: Self) -> Self:
        """Return the addition of two matrices"""
        return self._addition_subtraction(other, operator.add)

    def __sub__(self, other: Self) -> Self:
        """Return the subtraction of two matrices"""
        return self._addition_subtraction(other, operator.sub)

    def _matrix_multiplication(self, other: Self) -> Self:
        """Return the multiplication of two matrices"""
        return self.__class__(
            tuple(tuple(sum(n * m for n, m in zip(row, col)) for col in zip(*other._matrix)) for row in self._matrix))

    def __mul__(self, other) -> Self:
        """Return the multiplication of the matrix by scalar"""
        if isinstance(other, float):
            return self.__class__(tuple(tuple(n * other for n in row) for row in self._matrix))
        return self._matrix_multiplication(other)

    def __rmul__(self, other) -> Self:
        """Return the multiplication of the matrix by scalar"""
        return self.__mul__(other)

    def __truediv__(self, scalar: float) -> Self:
        """Return the division of the matrix by scalar"""
        return self.__mul__(1 / scalar)

    def __eq__(self, other: Self) -> bool:
        """Return True if two matrices are equal"""
        return self._matrix == other._matrix

    def __ne__(self, other):
        """Return True if two matrices are not equal"""
        return not self.__eq__(other)

    @classmethod
    def unity(cls, n: int):
        """Return the unity matrix of size n"""
        return cls(tuple(tuple(1 if i == j else 0 for i in range(n)) for j in range(n)))

    @classmethod
    def ones(cls, n: int):
        """Return the ones matrix of size n"""
        return cls(tuple(tuple(1 for i in range(n)) for j in range(n)))

    def __hash__(self):
        return hash(self._matrix)


if __name__ == '__main__':
    a = Matrix(((1, 2), (3, 4)))
    print(a)
    print(repr(a))
    print(a.tuples)
    b = Matrix(((2, 2), (2, 2)))
    print(b)
    print(Matrix.ones(3))

