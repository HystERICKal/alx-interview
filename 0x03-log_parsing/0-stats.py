#!/usr/bin/python3
"""Read stdin line by line."""


import sys


def stdin_reader(the_dict, complete_sof):
    """Read stdin line by line."""
    print("File size: {}".format(complete_sof))
    for i, j in sorted(the_dict.items()):
        if j != 0:
            print("{}: {}".format(i, j))


complete_sof = 0
the_num = 0
temp_1 = 0
the_dict = {"200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0}

try:
    for x in sys.stdin:
        extracted_sent = x.split()
        extracted_sent = extracted_sent[::-1]

        if len(extracted_sent) > 2:
            temp_1 += 1

            if temp_1 <= 10:
                complete_sof += int(extracted_sent[0])
                the_num = extracted_sent[1]

                if (the_num in the_dict.keys()):
                    the_dict[the_num] += 1

            if (temp_1 == 10):
                stdin_reader(the_dict, complete_sof)
                temp_1 = 0

finally:
    stdin_reader(the_dict, complete_sof)
