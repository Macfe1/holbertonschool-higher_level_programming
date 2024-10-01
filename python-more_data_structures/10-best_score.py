#!/usr/bin/python3
def best_score(a_dictionary):

    high_score = float('-inf')
    high_key = None

    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    else:
        for key, value in a_dictionary.items():
            if value > high_score:
                high_score = value
                high_key = key
    return high_key
