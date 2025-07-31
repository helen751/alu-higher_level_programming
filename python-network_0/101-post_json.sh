#!/bin/bash
# This script takes a URL and a JSON file as arguments
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
