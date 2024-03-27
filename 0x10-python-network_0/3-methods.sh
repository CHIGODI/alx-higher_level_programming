#!/bin/bash
# script takes in a URL and displays all HTTP methods the server will accept.

url="$1"

curl -sI -X OPTIONS "$url" | awk -F ':' '/Allow/ {print $2}'
