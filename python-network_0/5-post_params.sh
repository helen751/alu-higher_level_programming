#!/bin/bash
# This script takes a URL as an argument and sends a POST request
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
