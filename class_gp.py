from category import Category


class Store:
    def __init__(self, name, categories):
        # attributes
        # why do we underscore before an attribute name?
        self.name = name
        self.categories = categories

    # this prints out our description
    def __str__(self):
        string_output = ""
        string_output += "\n" + self.name + "\n\n" + "Categories:" + "\n"

        i = 0
        for category in self.categories:
            # why do i have to change this to category.name => right, i just want the property
            string_output += "   " + str(i) + ".   " + category.name + "\n"
            i += 1

            # string_output += "    " + str(i) + ". Exit"
        return string_output


my_store = Store("Cookies and Cream", [Category(
    "Cookies"), Category("Cream"), Category("Chocolate")])
print(my_store)

exit_key = len(my_store.categories)+2
selection = 0
selection_flag = True
while selection_flag:

    selection = input(
        f"Select the number of the department that you wish to access, from 1-3 . Press {exit_key} to exit out. \n")
    print(selection)
    try:
        selection = int(selection)
        if selection == exit_key:
            print("Thanks for shopping")
            selection_flag = False
            break
        elif selection > 0 and selection <= len(my_store.categories):
            print(my_store.categories[selection-1])
        else:
            print("Please select a valid number!")
    except ValueError:
        print("Please enter your choice as a number! Not a string. \n")
