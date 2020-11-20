# anagram_check - verifies if two strings are anagrams
# ignores whitespace

# import tests
from tests.tests import AnagramTest


# solution 1
def anagram(s1, s2):
    s1_dict = {}
    s2_dict = {}
    s1 = s1.lower()
    s2 = s2.lower()

    for char in s1:
        if char != ' ':
            if char not in s1_dict:
                s1_dict[char] = 1
            else:
                s1_dict[char] += 1

    for char in s2:
        if char != ' ':
            if char not in s2_dict:
                s2_dict[char] = 1
            else:
                s2_dict[char] += 1

    for key in s1_dict:
        if key not in s2_dict or s1_dict[key] != s2_dict[key]:
            return False

    return True


# solution 2
def anagram2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)


# solution 3
def anagram3(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # edge case check
    if len(s1) != len(s2):
        return False

    count = {}

    for char in s1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in s2:
        if char in count:
            count[char] -= 1
        else:
            count[char] = 1

    for key in count:
        if count[key] != 0:
            return False

    return True


# run tests
t = AnagramTest()
t.test(anagram)
