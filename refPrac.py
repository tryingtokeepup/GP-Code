
# this is simply passing the argument as a value


def multby10(x):
    return x * 10


number = 10

nate = multby10(number)

print(nate)
print(number)


def spam(eggs):
    eggs.append(1)
    eggs = [2, 3]
    # i think ham = [2,3]


ham = [0]
spam(ham)
print(ham)
