#!/usr/bin/python3
"""9-starwars.py"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get('https://swapi.co/api/people/?search=' + sys.argv[1])
    json_dict = r.json()
    res = json_dict['results']
    print('Number of results:', len(res))
    for ch in res:
        print(ch['name'])
