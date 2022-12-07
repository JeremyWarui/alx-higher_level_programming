#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    function that multiplies the values
    of dictionary by 2
    """
    copy = a_dictionary.copy()
    list_d = list(copy.keys())
    list_d.sort()
    for val in list_d:
        copy[val] *= 2
    return copy
