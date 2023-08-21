#!/usr/bin/python3
"""
Write a method that determines if a given data set represents
 a valid UTF-8 encoding.
    - Prototype: def validUTF8(data)
    - Return: True if data is a valid UTF-8 encoding, else return False
    - A character in UTF-8 can be 1 to 4 bytes long
    - The data set can contain multiple characters
    - The data will be represented by a list of integers
    - Each integer represents 1 byte of data, therefore you only need to
      handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    '''UTF-8 Validation'''
    def count_leading_ones(byte):
        mask = 1 << 7  # 10000000 in binary
        count = 0
        while byte & mask:
            count += 1
            mask >>= 1
        return count

    i = 0
    while i < len(data):
        leading_ones = count_leading_ones(data[i])

        if leading_ones == 0:
            i += 1
        elif leading_ones == 1 or leading_ones > 4:
            return False
        else:
            for j in range(1, leading_ones):
                if i + j >= len(data) or count_leading_ones(data[i + j]) != 1:
                    return False
            i += leading_ones
    return True
