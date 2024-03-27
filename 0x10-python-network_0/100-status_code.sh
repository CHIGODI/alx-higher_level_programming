#!/bin/bash
# prints status code of a http response
curl -sI "$1" | awk '/HTTP/ {print $2}'
