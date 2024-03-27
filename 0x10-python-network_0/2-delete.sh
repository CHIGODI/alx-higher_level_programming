#!/usr/bin/env bash
# use flag -X to specify http method

url="$1"

curl -sX DELETE "$url"
