#!/usr/bin/python3
class Student:
    """
    student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        my_dic = {}
        for key in self.__dict__:
            my_dic[key] = self.__dict__[key]
        return my_dic
