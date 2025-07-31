#!/bin/bash
# This script takes a URL as an argument and sends a PUT request
curl -s -X PUT -L -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me
