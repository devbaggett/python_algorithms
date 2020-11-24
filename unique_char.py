# unique_char

# Given a string,determine if it is comprised of all unique characters. For example, the string 'abcde' has all unique
# characters and should return True. The string 'aabcde' contains duplicate characters and should return false.

from tests.tests import TestUnique


def unique_char(string):
    unique_set = set()
    for char in string:
        if char not in unique_set:
            unique_set.add(char)
        else:
            return False
    return True


def unique_char2(string):
    return len(set(string)) == len(string)


t = TestUnique()
t.test(unique_char2)
