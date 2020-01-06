#!/bin/bash
#get cURL body size
curl -sI  "$1" | grep -i Allow | cut -d" " -f2
