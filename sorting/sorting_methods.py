# cool sorting methods
# sorting allows you to make solutions that will help you solve other problems TRIVIALLY
unsorted_numbers_list = [1, 8, 7, 3, 9, 6]
# to find the missing numbers
# sort the dumb thing
# sorted_numbers = [1, 2, 3, 4, 6, 7, 8, 9] no 5
# add up all these numbers, and compare them to the sum of 1 through 9, subtract the numbers from that sum, get the missing
# XOR this is actually how you do it with multiple
# XOR  and NOR allows modern computing

# 0 - 0 = 0
# 0 - 1 = 1 either true or false
# 1 - 0 = 1
# 1 - 1 = 0

phonebook = ["Generic 1000000 names inside here somehow lol"]


def name_in_phonebook(name_to_find):
    for name in phonebook:
        if name == name_to_find:
            return True
        else:
            return False


def name_in_phonebook_binary(phonebook, name):
    if len(phonebook) == 0:
        return False
    # set first element to 0
    first = 0

    # set last to size - 1
    last = (len(phonebook) - 1)

    # initialize fount to be False
    found = False
    # loop until you either find the name or reach the end of list
    while first <= last and not found:
        # find the middle of the list using integer division
        middle = (first + last) // 2
        # if found, update found variable
        if phonebook[middle] == name:
            found = True
        else:
            if name < phonebook[middle]:
                last = middle - 1
            else:
                first = middle + 1

    return found
