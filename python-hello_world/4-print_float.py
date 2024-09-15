#!/usr/bin/python3
number = 3.14159

try:
    cut_the_number = round(number, 2)
except(TypeError, ValueError) as round_err:
    print(f"Error in round: {round_err}")
    cut_the_number = None
try:
    if cut_the_number is not None:
        print(f"Float: {cut_the_number:.2f}")
    else:
        print("ValueError: Unknown format code 'f' for object of type 'str'")
except (TypeError, ValueError) as print_err:
    print (f"Error to print: {print_err}")
