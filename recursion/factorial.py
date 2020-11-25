# factorial

# Write a function factorial, which accepts a number and returns the factorial of that number. A factorial is the
# product of an integer and all the integers below it.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(4))  # 24
