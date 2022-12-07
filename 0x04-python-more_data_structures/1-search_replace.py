#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    function to search
    and replace the element in
    the list
    """
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list
