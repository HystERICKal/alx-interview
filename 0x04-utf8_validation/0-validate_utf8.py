#!/usr/bin/python3
"""Return True/False if UTF-8 Validation."""


def validUTF8(data):
    """Return True/False if UTF-8 Validation."""
    temp_1 = 0

    temp_2 = 1 << 7
    temp_3 = 1 << 6

    for x in data:

        temp_4 = 1 << 7

        if temp_1 == 0:

            while temp_4 & x:
                temp_1 += 1
                temp_4 = temp_4 >> 1

            if temp_1 == 0:
                continue

            if temp_1 == 1 or temp_1 > 4:
                return False

        else:
            if not (x & temp_2 and not (x & temp_3)):
                    return False

        temp_1 -= 1

    if temp_1 == 0:
        return True

    return False
