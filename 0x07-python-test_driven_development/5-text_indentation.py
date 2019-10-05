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
    for i in range(len(text)):
        if i > 0 and text[i] == ' ' and text[i - 1] in ".:?":
            continue
        print(text[i], end='')
        if text[i] in ".:?":
            print("\n")
