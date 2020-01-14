#!/usr/bin/python3
"""9-starwars.py"""
import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    api_token = sys.argv[2]
    api_url_base = 'https://api.github.com/user'

    r = requests.get(api_url_base, auth=(user, api_token))
    json_dict = r.json()
    print(json_dict.get('id'))
