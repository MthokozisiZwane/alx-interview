#!/usr/bin/python3
"""
Checks if a given data sets represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing bytes of data.

    Returns:
        True if data is a valid UTF-8 encoding, else returns False.
    """
    following_bytes = 0

    for byte in data:
        if following_bytes:
            if byte >> 6 != 0b10:
                return False
            following_bytes -= 1
        else:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 0b110:
                following_bytes = 1
            elif byte >> 4 == 0b1110:
                following_bytes = 2
            elif byte >> 3 == 0b11110:
                following_bytes = 3
            else:
                return False

    return following_bytes == 0
