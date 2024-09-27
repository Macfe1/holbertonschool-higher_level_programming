#!/usr/bin/python3
def multiple_returns(sentence):
    long = len(sentence)

    if long > 0:
        first = sentence[0]
    else:
        first = None

    new_tuple = (long, first)

    return new_tuple
