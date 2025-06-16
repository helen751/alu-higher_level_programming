#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        result += chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c
    print("{}".format(result))
