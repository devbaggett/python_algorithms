# sentence_reversal

# Given a string of words, reverse all the words. For example:

# Input: 'This is the best'
# Return: 'best the is This'

# As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

# '  space here'  and 'space here      '
# both become: 'here space'


from tests.tests import ReversalTest


def sentence_reversal(str):
    return " ".join(reversed(str.split()))


def sentence_reversal2(str):
    return " ".join(str.split()[::-1])


def sentence_reversal3(str):
    new_str = ""

    str_array = []
    for char in reversed(str):
        if char != " ":
            new_str = char + new_str
        else:
            if new_str:
                str_array.append(new_str)
                new_str = ""
    if new_str:
        str_array.append(new_str)

    new_str = str_array[0]
    for word in str_array[1:]:
        new_str += " " + word

    return new_str


def sentence_reversal4(str):
    words = []
    length = len(str)

    i = 0
    while i < length:
        if str[i] != " ":
            word_start = i
            while i < length and str[i] != " ":
                i += 1
            words.append(str[word_start:i])
        i += 1

    return " ".join(reversed(words))


t = ReversalTest()
t.test(sentence_reversal4)
