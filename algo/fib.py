# # this time around, let's do it together
# # we need to cache this somewhere?


def fib_bad(n):
    if n < 0:
        return print("please put in a non-neg number")
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_bad(n-1) + fib_bad(n-2)


def fib_memo(n):
    cache = {}  # O(1) Access and appending

    def fib_inner(n):
        nonlocal cache
        if n < 0:
            return print("please put in a non-neg number")
        if n < 2:
            return n

        # if n in cache:
        #     return cache[n]

        if n not in cache:
            cache[n] = fib_inner(n-1) + fib_inner(n-2)
        return cache[n]
    return fib_inner(n)


def fib_bottom_up(n):

    if n == 0:
        return 0
    if n == 1:
        return 1

    prev_value = 1
    prev_prev_value = 0
    i = 1

    while i < n:
        prev_prev_value, prev_value = prev_value, prev_value + prev_prev_value
        value = prev_value + prev_prev_value
        i += 1
    return value


for i in range(10):
    print(f"{i+1} : {fib_bottom_up(i)}")
