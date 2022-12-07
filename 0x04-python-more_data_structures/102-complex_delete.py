#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    function to delete all keys
    with specific value
    """
    for val in list(a_dictionary.keys()):
        if a_dictionary[val] is value:
            del a_dictionary[val]
        else:
            pass
    return a_dictionary
