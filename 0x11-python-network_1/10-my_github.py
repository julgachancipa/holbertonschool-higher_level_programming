#!/usr/bin/python3
"""9-starwars.py"""
import requests
import sys

if __name__ == "__main__":
    api_token = sys.argv[2]
    api_url_base = 'https://api.github.com/user'

    headers = {'Authorization': 'token ' + api_token}
    r = requests.get(api_url_base, headers=headers)
    json_dict = r.json()
    print(json_dict.get('id'))
