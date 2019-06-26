# good!


def factorial_recursive(n):
    # base case
    # and i have to call the factorial_recursive function inside this inner function

    if n == 0:
        return 1

    return n * factorial_recursive(n-1)


# def factorial_iterative(n):
#     accumlulator = 1
#     if n == 0:
#         return 1  # already, if the guy is mean enough to throw 0 into here, we're ready
#     for i in range(n, 1, -1):
#         accumlulator *= i
#         print(
#             f"The factorial of {n - i + 2 }, when done iteratively, is {accumlulator} \n")
#     return accumlulator


# print(factorial_recursive(5))

# exponentials?????
def exponential_recusion(a, b):

    if b == 0:
        return 1
    # if b == 1:
    #     return a

    return a * exponential_recusion(a, b-1)


print(exponential_recusion(2, 4))
