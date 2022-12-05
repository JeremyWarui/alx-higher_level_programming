#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    function to return the max integer in the list
    """
    nums = len(my_list)
    max_num = my_list[0]
    if nums == 0:
        return None
    else:
        for n in my_list:
            if n > max_num:
                max_num = n
    return max_num
