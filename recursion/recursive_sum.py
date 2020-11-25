# recursive_sum

# Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer

# For example, if n=4 , return 4+3+2+1+0, which is 10.

def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)


print(recursive_sum(5))  # 15
