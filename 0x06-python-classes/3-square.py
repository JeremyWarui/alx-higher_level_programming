#!/usr/bin/python3
"""
Module: Square class
"""


class Square:
    """
    Class Square that defines square object

    Args:
        size (int): size of a side in square
    Methods:
        area(self)
    """
    def __init__(self, size=0):
        """
        Initilize the size to 0 if None
        """
        if isinstance(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Method:
            Calculate the area of the square given the size

        Args:
            The class object with all is properties
        Returns:
            Area of square
        """
        return self.__size ** 2
