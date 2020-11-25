# word_split

# Create a function called word_split() which takes in a string phrase and a set list_of_words. The function will then
# determine if it is possible to split the string in a way in which words can be made from the list of words. You can
# assume the phrase will only contain words found in the dictionary if it is completely splittable.


def word_split(string, word_list, output=None):
    if output is None:
        output = []
    for word in word_list:
        if string.startswith(word):
            output.append(word)
            return word_split(string[len(word):], word_list, output)

    return output


print(word_split('themanran', ['the', 'ran', 'man']))  # ['the', 'man', 'ran']
print(word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']))  # ['i', 'love', 'dogs', 'John']
print(word_split('themanran', ['clown', 'ran', 'man']))  # []
