# # lets create a new list, and our goal is to square every single number in the list

numbers = [17, 8, 97, 30, 2]
numbers[0] = 29
print(numbers)



# squares = [number * number for number in numbers]

# print(squares)

# odds = [number for number in numbers if number % 2 == 1]

# print(odds)

# # why was it not allowing us to use "not" inside our comparision
# # when can "not" be used in a function? is it only for the looping logic, or comparisions?
# odds_squares = [number for number in squares if not number % 2 == 0]

# print(odds_squares)

# names = ["Kai", "Tyler", "Sarah", "Jermaine",
#          "Madoka", "fukuoka", "Fuji", "Sylvester", "fred"]


# f_names = [name.capitalize() for name in names if name[0].lower() == "f"]

# print(f_names)

# y_will_wait_for_input_while_user_puts_this_in = input(
#     "Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
# whoops, seems like you need to cast all of the is to make this work
# for you to do "work" on some sort of data, the data must be in the right format
# y = [number for number in y_will_wait_for_input_while_user_puts_this_in if int(
#     number) % 2 == 0]

# print(y)
