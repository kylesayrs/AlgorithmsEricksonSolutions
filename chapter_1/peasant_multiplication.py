from typing import List


def peasant_multiplication(x: int, y: int) -> int:
    """
    x * y = 0               if x == 0 or y == 0
    x * y = y               if x == 1
    x * y = x//2 * (2y)     if x is even
    x * y = x//2 * (2y) + y if x is odd
    """
    if x == 0 or y == 0:
        return 0
    
    if x == 1:
        return y
    
    if x & 1 == 0:
        return peasant_multiplication(x >> 1, y + y)
    else:
        return peasant_multiplication(x >> 1, y + y) + y
    

def peasant_multiplication(x: int, y: int) -> int:
    """
    x * y = 0               if x == 0 or y == 0
    x * y = y               if x == 1
    x * y = x//2 * (2y)     if x is even
    x * y = x//2 * (2y) + y if x is odd

    The table visualization in the book is good. I like to think of going from
    the recursive implementation to the iterative implementation as similar to
    implementing the algorithm on the level of assembly.

    On each recursive call, we load the next call's values into the registers.
    Once we load the registers, we call the function again.

    Since the outer layer (+ y) is commutative, we can use an accumulator register.

    This approach saves stack memory by reusing variables
    """
    result = 0
    while x > 0:
        if x & 1 == 1:
            result += y

        x = x >> 1
        y = y + y

    return result


if __name__ == "__main__":
    for x in [0, 1, 2, 5, 10, 500]:
        for y in [0, 1, 2, 5, 10, 500]:
            assert peasant_multiplication(x, y) == x * y
