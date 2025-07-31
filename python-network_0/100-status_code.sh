#!/bin/bash
# This script takes a URL as an argument and returns the HTTP status code
curl -s -o /dev/null -w "%{http_code}" "$1"
