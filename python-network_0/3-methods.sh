#!/bin/bash
# This script takes a URL as an argument and returns the allowed HTTP methods
curl -sI "$1" | grep -i '^Allow:' | cut -d' ' -f2-