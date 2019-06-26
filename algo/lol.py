

def longest_string(arr):

    min = 0
    longest = ""
    for string in arr:
        if len(string) > min:
            min = len(string)
            longest = string

    return longest


print(longest_string(["Kai is cool", "He eats lots of chocolate.", "Happy!"]))
