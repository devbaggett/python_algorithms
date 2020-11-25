# Write a function that, given an array A of N integers, returns the smallest positive integer (greater than 0) that
# does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.

# Assumptions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].


def smallest_positive_integer(A):
    smallest = 1
    unique = set(A)
    for int in unique:
        if int == smallest:
            smallest += 1
    return smallest


print(smallest_positive_integer([1, 3, 6, 4, 1, 2]))  # 5
print(smallest_positive_integer([1, 2, 3]))  # 4
print(smallest_positive_integer([-1, 3]))  # 1
