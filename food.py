from product import Product


class Food(Product):
    def __init__(self, name, description, price, cuisine):
        super().__init__(name, description, price)
        self.cuisine = cuisine

    def __str__(self):
        return super().__str__() + "\tThis food is a " + self.cuisine + " cuisine!"


new_food = Food("Tacos", "Its a taco.", "1000 dollars", "Baddbutt Mexican")
print(new_food)
