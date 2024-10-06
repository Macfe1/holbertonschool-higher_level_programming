#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0

    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))

    return result


if __name__ == "__main__":
    safe_print_division(10, a)
