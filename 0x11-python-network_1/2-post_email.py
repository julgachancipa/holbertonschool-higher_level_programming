#!/usr/bin/python3
"""2-post_email.py"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    post_url = sys.argv[1]
    email = sys.argv[2]
    post_data = parse.urlencode({'email': email}).encode('utf-8')
    with request.urlopen(url=post_url, data=post_data) as response:
        print(response.read().decode('utf-8'))
