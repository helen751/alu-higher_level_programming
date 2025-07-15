#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""
import sys

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
total_size = 0
count = 0

def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))

try:
    for line in sys.stdin:
        count += 1
        parts = line.split()
        if len(parts) > 6:
            code = parts[-2]
            size = parts[-1]
            try:
                total_size += int(size)
            except Exception:
                pass
            if code in status_codes:
                status_codes[code] += 1
        if count % 10 == 0:
            print_stats()
    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
