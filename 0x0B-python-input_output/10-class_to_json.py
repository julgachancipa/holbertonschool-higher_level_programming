#!/usr/bin/python3
def class_to_json(obj):
    flag = 0
    my_str = '{'
    for key in obj.__dict__:
        if flag:
            my_str += ', '
        flag = 1
        my_str += '\''
        my_str += key
        my_str += '\': '
        my_str += str(obj.__dict__[key])
    my_str += '}'
    return my_str
