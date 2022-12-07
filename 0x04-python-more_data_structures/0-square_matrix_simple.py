#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    function thhat return square of all matrix values
    """
    if len(matrix) != 0:
        copy = matrix[:]
        new_list = []
        for nlist in matrix:
            copy = list(map(lambda x: x * x, nlist))
            new_list.append(copy)
        return new_list
    # return list(map(lambda x: list(map(lambda x: x * x, x)), matrix))
