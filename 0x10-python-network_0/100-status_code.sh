#!/bin/bash
# prints status code of a http response

url="$1"

curl -sI "${url}" | awk '/HTTP/ {print $2}'
