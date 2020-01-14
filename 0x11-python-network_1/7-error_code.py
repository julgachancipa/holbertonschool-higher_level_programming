#!/usr/bin/python3
"""7-error_code.py"""
import requests
from requests.exceptions import HTTPError
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except HTTPError as e:
        print('Error code:', response.status_code)
