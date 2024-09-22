#!/usr/bin/python3
import sys


if __name__ == "__main__":
    suma = 0

    for iterator in range(1, len(sys.argv)):
        suma += int(sys.argv[iterator])
    print(suma)
