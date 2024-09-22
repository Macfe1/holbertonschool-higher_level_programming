#!/usr/bin/python3
import sys

if __name__ == "__main__":
    number_args = len(sys.argv) - 1

    if number_args == 0:
        print("0 arguments.")
    elif number_args == 1:
        print("1 arguments:")
    elif number_args > 1:
        print("{} arguments:".format(number_args))

    for iterator in range(1, len(sys.argv)):
        print("{}: {}".format(iterator, sys.argv[iterator]))
