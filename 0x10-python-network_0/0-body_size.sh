#!/bin/bash
# displays the size of the body of GET response

URL="$1"

curl -sI "$URL" | awk '/Content-Length/ {print$2}'
