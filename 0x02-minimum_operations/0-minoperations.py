#!/usr/bin/python3
"""
Module for calculating minimum operations to achieve desired number
of characters
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file.

    Args:
        n (int): The desired number of chars

    Returns:
        int: The minimum number of operations needed,
        or 0 if it's impossible to achieve n characters.
    """
    if n <= 1:
        return 0

    number_operations = 0
    count_h = 1
    copied_h = 0

    while count_h < n:
        if n % count_h == 0:
            copied_h = count_h
            number_operations += 1

        count_h += copied_h
        number_operations += 1

    if count_h == n:
        return number_operations
    else:
        return 0
