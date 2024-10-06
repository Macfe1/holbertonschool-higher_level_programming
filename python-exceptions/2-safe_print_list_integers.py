#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0

    while counter < x:
        try:
            print("{:d}".format(my_list[counter]), end="")
            counter += 1
        except (ValueError, TypeError):
            counter += 1
        except IndexError:
            break
    print()
    return counter


if __name__ == "__main__":
    safe_print_list_integers([1, 2, 3, "Hola"], 4)
