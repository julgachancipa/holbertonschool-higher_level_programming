#!/bin/bash
#get cURL body size
curl -siLX OPTIONS "$1" | grep Allow | cut -d' ' -f2-
