#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    function to add new element in a given index
    """
    copy = my_list[:]
    if 0 <= idx < len(my_list):
        copy[idx] = element
        return copy
