#!/usr/bin/python3
"""
Prototype: def text_indentation(text):
text must be a string, otherwise raise a TypeError
exception with the message text must be a string
"""


def text_indentation(text):
    """
    prints 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 1
    for l in text:
        if flag:
            print(l, end='')
        if l in ".?:":
            flag = 0
            print('\n')
        else:
            flag = 1
