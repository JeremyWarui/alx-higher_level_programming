#!/usr/bin/python3
"""
3-square: defines square with private attribute size and public attribute area
"""


class Square:
    """
    Class square defination

    Args:
        size: size of a side of square

    Functions:
        __init__(self, size)
        area(self)
    """

    def __init__(self, size=0):
        """
        Initilization square

        Attributes:
            __size: size of a side of square, defaults to 0 if None
        """
        if isinstance(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calculates area of square

        Returns:
            area
        """
        return (self.__self)**2
