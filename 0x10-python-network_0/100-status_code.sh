#!/bin/bash
# prints status code of a http response
curl -s -o /dev/null -w "%{http_code}" $1
