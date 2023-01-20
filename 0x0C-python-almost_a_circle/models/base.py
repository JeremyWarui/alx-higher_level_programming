#!/usr/bin/python3
""" Module: Base """


import json


class Base():
    """
    A base model class
    Private class attribute: __nb_objects (int)
    Public class attribute: id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialise instances"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ 
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
