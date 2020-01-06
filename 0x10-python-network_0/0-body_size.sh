#!/bin/bash
#get cURL body size

curl -sI  "$1" | grep -i Content-Length | grep -o '[0-9]\+'
