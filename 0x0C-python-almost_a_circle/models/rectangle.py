#!/usr/bin/python3
"""
Module: Rectangle
Inherits from Base;
Initialise superclass' id
"""

from models.base import Base


class Rectangle(Base):
    """
    class Rectangle
    Inherited Attributes: id
    Private attributes: __width, __height,
    __x, __y
    Methods:
        update, width, width(self, value), height(self),
        height(self, value), x(self), x(self, value), y(self),
        y(self, value), area(self), display(self), __str__,
        to_dictionary(self)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialise intances """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ GETTERS """

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @property
    def x(self):
        """ getter for x """
        return self.__x

    @property
    def y(self):
        """ getter for y """
        return self.__y

    """ SETTERS """

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """ METHODS """

    def area(self):
        """ function to return area """
        return self.__width * self.__height

    def display(self):
        """
        Print out the instance to stdout using #'s
        """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """ Prints [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args):
        """ update the attributes """
        arg_list = []
        for i in args:
            arg_list.append(i)
        len_args = len(arg_list)
        if len_args > 0:
            self.id = arg_list[0]
            len_args -= 1
        if len_args > 0:
            self.__width = arg_list[1]
            len_args -= 1
        if len_args > 0:
            self.__height = arg_list[2]
            len_args -= 1
        if len_args > 0:
            self.__x = arg_list[3]
            len_args -= 1
        if len_args > 0:
            self.__y = arg_list[4]
