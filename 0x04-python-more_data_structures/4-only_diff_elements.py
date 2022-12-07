#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    function to find the difference in two sets
    """
    new = set_1.symmetric_difference(set_2)
    return list(new)
