#!/usr/bin/python3
import os.path
from sys import argv


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


def upgeral():
    """
    update list
    """
    li = []
    f = 'add_item.json'
    i = 1
    l = len(argv)
    if os.path.isfile(f):
        li = load_from_json_file(f)
        while i < l:
            li.append(argv[i])
            save_to_json_file(li, f)
            i += 1
    else:
        open(f, 'w')
        save_to_json_file(li, f)
        while i < l:
            li.append(argv[i])
            save_to_json_file(li, f)
            i += 1

if __name__ == '__main__':
    upgeral()
