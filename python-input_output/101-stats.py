#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys


def print_stats(total_size, status_codes):
    """Prints the total file size and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


total_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 7:
            try:
                size = int(parts[-1])
                code = parts[-2]
                total_size += size
                if code in status_codes:
                    status_codes[code] += 1
            except Exception:
                pass
            count += 1
        if count == 10:
            print_stats(total_size, status_codes)
            count = 0
except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise

print_stats(total_size, status_codes)
