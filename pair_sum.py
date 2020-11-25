# pair_sum

# Given an integer array, output all the ** unique ** pairs that sum up to a specific value k.

# So the input:
# pair_sum([1,3,2,2],4) would return 2 pairs: (1,3), (2,2)

# NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS

from tests.tests import TestPair


def pair_sum(arr, k):
    count = 0

    pairs = {}
    for i in arr:
        for j in arr:
            if i + j == k:
                pair = tuple(sorted((i, j)))
                if pair not in pairs:
                    pairs[pair] = True
                    count += 1

    return count


def pair_sum2(arr, k):
    if len(arr) < 2:
        return False

    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    # print('\n'.join(map(str,list(output))))
    return len(output)


def pair_sum3(array, k):
    pairs = set()
    for i in array:
        for j in array:
            if i + j == k:
                pair = tuple(sorted((i, j)))
                pairs.add(pair)

    return len(pairs)


# pair_sum2([1, 3, 2, 2], 4) # 2
# pair_sum([1, 2, 3, 1], 3) # 1

# Run tests
t = TestPair()
t.test(pair_sum3)
