#!/usr/bin/python3
"""
   module perfoming division to elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    matrix: a list of integers or floats
    div: what will be used in division
    """
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # ensures a fixed comparison incase matrix changes
    first_length = len(matrix[0])
    for row in matrix:
        if len(row) != first_length:
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if not isinstance(num, (float, int)):
                raise TypeError("matrix must be a matrix (list of lists) of"
                                " integers/floats")
    result = list(list(map(lambda num: round((num / div), 2), row))for
                  row in matrix)

    return result
