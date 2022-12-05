#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    function to add new element in a given index
    """
    copy = my_list[:]
    if not my_list:
        pass
    elif idx <= 0:
        return copy
    elif idx > len(my_list):
        return copy
    else:
        copy[idx] = element
        return copy
