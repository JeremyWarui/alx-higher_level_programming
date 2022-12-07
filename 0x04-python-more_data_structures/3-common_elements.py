#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    function to check for similar elements in dffrt sets
    """
    common = set_1.intersection(set_2)
    return list(common)
