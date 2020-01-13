#!/usr/bin/python3
"""5-hbtn_header.py"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
