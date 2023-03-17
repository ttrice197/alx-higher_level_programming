#!/usr/bin/python3
def print_sorted_dictionar(a_dictionary):
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
