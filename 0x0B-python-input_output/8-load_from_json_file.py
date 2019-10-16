#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    """
    with open(filename, encoding="utf-8") as myFile:
        my_str = myFile.read()
        return json.loads(my_str)
