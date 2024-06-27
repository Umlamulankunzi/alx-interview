#!/usr/bin/python3
"""
Script Determines if given data is valid utf8.
"""


def validUTF8(data):
    """Verifies if data is valid utf8 format. 

    Returns true if data is valid utf8
    """

    num_bytes = 0

    for num in data:
        binary_res = format(num, '#010b')[-8:]

        if num_bytes == 0:
            for bit in binary_res:
                if bit == '0':
                    break
                num_bytes += 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (binary_res[0] == '1' and binary_res[1] == '0'):
                return False

        num_bytes -= 1

    return num_bytes == 0
