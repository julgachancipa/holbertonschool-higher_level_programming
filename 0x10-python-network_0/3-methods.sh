#!/bin/bash
#get cURL body size
curl -sX OPTIONS "$1" -i | grep -i Allow | cut -f 1 -d ' ' --complement
