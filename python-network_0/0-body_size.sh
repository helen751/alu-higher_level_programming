#!/bin/bash
# This script takes a URL as an argument and returns the size of the body in bytes.
curl -s "$1" | wc -c
