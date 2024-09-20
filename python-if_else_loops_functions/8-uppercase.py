#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for letras in range(len(str)):
        to_upper = ord(str[letras])
        if to_upper > 96 and to_upper < 123:
            to_upper = to_upper - 32
        new_str += chr(to_upper)
    print("{}".format(new_str))
