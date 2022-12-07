#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if a_dictionary is None or a_dictionary == {}:
        return None
    biggest = max(a_dictionary.values())
    for key, value in a_dictonary.items():
        if value is biggest:
            return key
