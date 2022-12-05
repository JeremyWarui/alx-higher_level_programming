#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    function to return the max integer in the list
    """
    nlen = len(my_list)
    max_num = my_list[0]
    if nlen == 0:
        return None
    else:
        for num in my_list:
            if num >= max_num:
                max_num = num
    return max_num
