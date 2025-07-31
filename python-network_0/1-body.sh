#!/bin/bash
curl -s -L -w "%{http_code}" "$1" | { read body; code="${body: -3}"; if [ "$code" = "200" ]; then echo "${body%???}"; fi; }
