#!/usr/bin/python3
"""
first class Base
"""
import json
import os.path


class Base:
    """
    first class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init method
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to json m
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        to file method
        """
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

    @staticmethod
    def from_json_string(json_string):
        """
        from json
        """
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create method
        """
        ex = cls(1, 1, 1)
        ex.update(**dictionary)
        return ex

    @classmethod
    def load_from_file(cls):
        """
        from file
        """
        lst = []
        if os.path.isfile(cls.__name__ + '.json'):
            with open(cls.__name__ + ".json",
                      encoding='utf-8') as json_f:
                json_str = json_f.read()
                obj_dics = cls.from_json_string(json_str)
                for dicts in obj_dics:
                    lst.append(cls.create(**dicts))
                return lst
        else:
            return lst
