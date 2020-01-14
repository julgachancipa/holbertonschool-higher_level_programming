#!/usr/bin/python3
"""8-json_api.py"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = {'q': sys.argv[1]}
    else:
        q = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', q)
    json_dict = r.json()
    if json_dict is None:
        print('Not a valid JSON')
    try:
        print('[{}] {}'.format(json_dict['id'], json_dict['name']))
    except:
        print('No result')
