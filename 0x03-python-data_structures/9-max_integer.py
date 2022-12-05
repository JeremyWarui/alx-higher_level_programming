#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    function to return the max integer in the list
    """
    nums = len(my_list)
    max_num = 0
    if nums == 0:
        return None
    else:
        for num in range(1, nums):
            if my_list[num] > max_num:
                max_num = my_list[num]
    return max_num
