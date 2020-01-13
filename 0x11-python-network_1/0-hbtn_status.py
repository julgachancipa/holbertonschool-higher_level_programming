#!/usr/bin/python3
"""0-hbtn_status.py"""
from urllib import request


with request.urlopen('https://intranet.hbtn.io/status') as response:
    x = response.read()
    print('Body response:')
    print('\t- type: ', end='')
    print(type(x))
    print('\t- content: ', end='')
    print(x)
    print('\t- utf8 content: ' + x.decode('utf-8'))
