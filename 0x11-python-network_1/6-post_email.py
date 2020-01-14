#!/usr/bin/python3
"""5-hbtn_header"""
import requests
import sys


if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], email)
    print(r.text)
