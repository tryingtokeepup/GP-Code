# # recursive sorting

# # What is recursion?


# def fib(n):

#     if n >= 2:
#         return n

#     return fib(n-1) + fib(n-2)


# # Nate, you are 10000000 precent correct
# # Code that calls itself
# # It needs a base case to prevent itself from recurssing forever
# # Stack Overflow
# # It makes for clean, elegant code
# # but, it's not very space performant
# # In Web, we use recursion all the time to get queries to the APIs that we handle

# #

# def foo(n):  # O(2^n)
#     if n <= 0:
#         return
#     print(n)

#     foo(n-1)
#     foo(n-2)


# n = 10
# print(foo(n))


# # Sorting tends to lend itself very well to recursion

# # Recap on insertion sort
# [3, 4, 5, 6, 10]
# # THE WORD SWAP BASICALLY INDICATES IMPLICITLY that i am using a TEMP VARIABLE


# def insertion_sort(arr):
#     # loop through n-1 elements
#     # we need to have the left side of the array be our "sorted array"
#     for i in range(1, len(arr)):
#         temp = arr[i]  # at the start, it would be array[1]
#         j = i

#         # always check if the element before j is in the right spot
#         while j > 0 and temp < arr[j - 1]:
#             # shift left until correct position is found
#             arr[j] = arr[j - 1]
#             j -= 1
#             # insert at correct position
#             arr[j] = temp
#         return arr

# Base Case so that we can leave the function
# Inner body of the function => Call the function inside it

# start by choosing a pivot
# this can be the first or last element
# the middle, median, or random element usually performs better (tends to split the original data more evenly)
# b. Move all elements smaller than the pivot to its left hand side. move all elements larger than pivot to its right hand side.
# c. recursively quick sort LHS and RHS until (some base case) where a side only contains a single element

# sorted_thingy [1][2] [3][4][5][6]


def partition(data):

    left = []
    pivot = data[0]
    right = []

    for variable in data[1:]:
        if variable <= pivot:
            left.append(variable)
        else:
            right.append(variable)

    return left, pivot, right


def quicksort(data):
    if data == []:
        return data
    left, pivot, right = partition(data)

    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([5, 9, 3, 7, 2, 8, 1, 6]))
