#!/usr/bin/python3

def islower(c):
    value_ascii = ord(c)
    if value_ascii < 97 or value_ascii > 122:
        return False
    else:
        return True
