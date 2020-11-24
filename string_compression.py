# stringCompression

# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely
# "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this
# technically takes more space.

# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

from tests.tests import TestCompress
from collections import Counter


# not taking in account order
def string_compression(string):
    char_counts = Counter(string)
    return ''.join('{}{}'.format(key, value) for key, value in char_counts.items())


# taking in account order
def string_compression2(string):
    new_str = ""

    length = len(string)
    if length == 0:
        return ""
    if length == 1:
        return string + "1"

    count = 1
    i = 1
    while i < length:
        if string[i] == string[i - 1]:
            count += 1
        else:
            new_str += string[i - 1] + str(count)
            count = 1
        i += 1

    new_str += string[i - 1] + str(count)

    return new_str


t = TestCompress()
t.test(string_compression2)
