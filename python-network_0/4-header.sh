#!/bin/bash
# This script takes a URL as an argument and sends a GET request with a custom header
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"