# find_missing_element

# Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and
# deleting a random element. Given these two arrays, find which element is missing in the second array.

# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

# Input: finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
# Output: 5 is the missing number

from tests.tests import TestFinder
import collections


# O(n + m)
def finder(arr1, arr2):
    if arr1 == arr2:
        return False

    dict = {}
    for num in arr2:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1

    for num in arr1:
        if num not in dict:
            return num
        elif dict[num] == 1:
            del dict[num]
        else:
            dict[num] -= 1

    return False


# O(n log n)
def finder1(arr1, arr2):
    arr1.sort()
    arr2.sort()
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    return arr1[-1]


def finder3(arr1, arr2):
    dict = collections.defaultdict(int)
    for num in arr2:
        dict[num] += 1
    for num in arr1:
        if dict[num] == 0:
            return num
        else:
            dict[num] -= 1


def finder4(arr1, arr2):
    result = 0

    # perform an XOR between numbers in arrays
    for num in arr1 + arr2:
        result ^= num
        print(num, result)

    return result


# print(finder4([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])) # 5
# print(finder3([5, 5, 7, 7], [5, 7, 7])) # 5

t = TestFinder()
t.test(finder3)
