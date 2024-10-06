#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_div = []

    for iterator in range(list_length):
        result = 0

        try:

            element_first_list = my_list_1[iterator]
            element_second_list = my_list_2[iterator]

            if not isinstance(element_first_list, (int, float)):
                raise TypeError
            if not isinstance(element_second_list, (int, float)):
                raise TypeError

            result = element_first_list / element_second_list

        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            list_div.append(result)

    return list_div


if __name__ == "__main__":
    list_1 = [10, 8, 4, 4]
    list_2 = [2, 0, "H", 2, 7]
    result = list_division(list_1, list_2, max(len(list_1), len(list_2)))
    print(result)
