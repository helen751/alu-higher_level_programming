#!/bin/bash
# This script takes a URL as an argument and sends a PUT request
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
