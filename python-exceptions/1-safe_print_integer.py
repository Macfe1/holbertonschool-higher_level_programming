#!/usr/bin/python3
def safe_print_integer(value):
    if isinstance(value, int):
        try:
            print("{:d}".format(value))
            return True
        except TypeError:
            return False


if __name__ == "__main__":
    safe_print_integer(1)
