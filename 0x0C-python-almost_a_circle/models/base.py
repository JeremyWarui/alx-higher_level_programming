#!/usr/bin/python3
""" Module: Base """


import json
import csv
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        obj = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                for i in list_objs:
                    obj.append(i.to_dictionary())
                lists = cls.to_json_string(obj)
                f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes
        """
        if cls.__name__ == "Rectangle":
            inst = cls(1, 1)
        if cls.__name__ == "Square":
            inst = cls(1)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"
        list_ins = []
        if os.path.isfile(filename):
            with open(filename, 'r', encoding="utf-8") as f:
                list_str = f.read()
            list_cls = cls.from_json_string(list_str)
            for dictionary in list_cls:
                list_ins.append(cls.create(**dictionary))
            return list_ins
        else:
            return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV """
        filename = cls.__name__ + ".csv"
        name = cls.__name__
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for i in list_objs:
                if name == "Rectangle":
                    writer.writerow([i.id, i.width, i.height, i.x, i.y])
                if name == "Square":
                    writer.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        objs = []
        name = cls.__name__
        filename = name + ".csv"
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if name == "Rectangle":
                    dic = {"id": int(row[0]),
                           "width": int(row[1]),
                           "height": int(row[2]),
                           "x": int(row[3]),
                           "y": int(row[4])}
                if name == "Square":
                    dic = {"id": int(row[0]),
                           "size": int(row[1]),
                           "x": int(row[2]),
                           "y": int(row[3])}
                objs.append(cls.create(**dic))
        return objs
