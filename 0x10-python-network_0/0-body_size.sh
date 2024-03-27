#!/bin/bash
# displays the size of the body of GET response
curl -sI "$1" | awk '/Content-Length/ {print$2}'
