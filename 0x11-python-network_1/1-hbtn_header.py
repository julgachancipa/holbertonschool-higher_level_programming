#!/usr/bin/python3
"""1-hbtn_header.py"""
from urllib import request
import sys


with request.urlopen(sys.argv[1]) as response:
    print(response.headers['X-Request-Id'])
