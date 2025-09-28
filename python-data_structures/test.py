#!/usr/bin/python3
def test():
    my_tupla = ('Hola', 1, 10)

    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

    print(my_tupla)
    
    for row in matrix:
        for columns in row:
            print(columns, end=" ")

test()
