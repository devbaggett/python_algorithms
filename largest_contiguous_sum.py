# largest_contiguous_sum

# Given an array of integers (positive and negative) find the largest continuous sum.

from tests.tests import LargeContTest


def largest_contiguous_sum(arr):
    if len(arr) == 0:
        return None

    start = arr[0]
    end = len(arr) - 1
    largest_sum = arr[0]
    current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        largest_sum = max(current_sum, largest_sum)

    return largest_sum


# print(largest_contiguous_sum([1, 2, -1, 3, 4, -1]))  # 9

t = LargeContTest()
t.test(largest_contiguous_sum)
