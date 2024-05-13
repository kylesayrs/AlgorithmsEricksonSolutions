import numpy


def exponentiation_matrix(a: numpy.ndarray, n: int) -> numpy.ndarray:
    """
    a^0 = 1
    a^1 = a
    a^n = a^(n // 2) * a^(n // 2)      if n is even
    a^n = a^(n // 2) * a^(n // 2) * a  if n is odd
    """
    if n == 0:
        return numpy.eye(a.shape[0], dtype=numpy.int32)

    a_sqrt = peasant_exponentiation_matrix(a, n >> 1)

    if n & 1 == 0:
        return a_sqrt @ a_sqrt
    
    else:
        return a_sqrt @ a_sqrt @ a


def peasant_exponentiation_matrix(a: numpy.ndarray, n: int) -> numpy.ndarray:
    """
    x^0 = 1
    x^1 = a
    x^y = (x * x)^(y // 2)     if n is even
    x^y = (x * x)^(y // 2) * x if n is odd
    """
    result = numpy.eye(a.shape[0], dtype=numpy.int32)

    x = a
    y = n
    while y > 0:
        if y & 1 == 1:
            result @= x

        x = x @ x
        y = y >> 1

    return result


def fast_fib(n: int) -> int:
    """
    [[0, 1]       [x      [y
     [1, 1]]  @    y]  =   z]
    """
    if n == 0:
        return 0

    matrix = numpy.array([[0, 1], [1, 1]])
    
    matrix_exp = peasant_exponentiation_matrix(matrix, n)

    _f_minus_1, f = matrix_exp @ numpy.array([0, 1])

    return f


if __name__ == "__main__":
    assert peasant_exponentiation_matrix(numpy.array([[1]]), 10) == numpy.array([[1]])
    assert peasant_exponentiation_matrix(numpy.array([[2]]), 10) == numpy.array([[2 ** 10]])
    assert numpy.all(peasant_exponentiation_matrix(numpy.array([[1, 0], [0, 1]]), 10) == numpy.array([[1, 0], [0, 1]]))

    assert fast_fib(0) == 0
    assert fast_fib(1) == 1
    assert fast_fib(2) == 2
    assert fast_fib(3) == 3
    assert fast_fib(4) == 5
    assert fast_fib(5) == 8
