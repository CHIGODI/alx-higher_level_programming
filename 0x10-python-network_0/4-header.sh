#!/usr/bin/env bash
#  sends a GET request to the URL, and displays the body of the response
#A header variable X-School-User-Id must be sent with the value 98

url="$1"

curl -sH X-School-User-Id:98 "$url"
