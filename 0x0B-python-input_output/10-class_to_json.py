#!/usr/bin/python3
def class_to_json(obj):
    my_dic = {}
    for key in obj.__dict__:
        my_dic[key] = obj.__dict__[key]
    return my_dic
