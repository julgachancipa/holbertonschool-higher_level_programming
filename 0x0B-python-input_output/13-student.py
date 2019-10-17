#!/usr/bin/python3
class Student:
    """
    student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_dic = {}
        if attrs is not None:
            for i in range(0, len(attrs)):
                if attrs[i] in self.__dict__:
                    my_dic[attrs[i]] = self.__dict__[attrs[i]]
                    i += 1
        else:
            for key in self.__dict__:
                my_dic[key] = self.__dict__[key]
        return my_dic

    def reload_from_json(self, json):
        l = list(json.keys())
        original = self.__dict__
        for k in l:
            original[k] = json.get(k)
