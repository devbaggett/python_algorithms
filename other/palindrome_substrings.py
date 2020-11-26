# Assorted palindrome substring functions

def find_unique_palindrome_substrings(string):
    subs = []

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            sub = ''.join(string[i:j])
            if str(sub) == str(sub)[::-1] and len(sub) > 1:
                subs.append(sub)

    return list(set(subs))


def longest_palindrome_substring(string):
    longest = ""

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            sub = ''.join(string[i:j])
            if str(sub) == str(sub)[::-1]:
                if len(sub) > len(longest):
                    longest = sub

    return longest


def count_palindrome_substrings(string):
    substrings = set()

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            sub = ''.join(string[i:j])
            if str(sub) == str(sub)[::-1] and len(sub) > 1:
                substrings.add(sub)

    return len(substrings)


print(find_unique_palindrome_substrings("10101"))
print(find_unique_palindrome_substrings("101"))
print(longest_palindrome_substring("10101"))
print(count_palindrome_substrings("10101"))
