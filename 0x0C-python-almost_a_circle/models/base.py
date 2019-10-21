#!/usr/bin/python3
"""
first class Base
"""
import json


class Base:
    """
    first class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is not None and len(list_objs) > 0:
            lst = []
            for obj in list_objs:
                json_dict = obj.to_dictionary()
                lst.append(json_dict)
            with open(cls.__name__ + ".json", mode='w',
                      encoding='utf-8') as json_f:
                json_f.write(cls.to_json_string(lst))
        else:
            with open(cls.__name__ + ".json", mode='w',
                      encoding='utf-8') as json_f:
                json_f.write(cls.to_json_string(list_objs))
