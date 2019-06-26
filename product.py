

class Product:
    def __init__(self, name, description, price, popularity=None):
        self.name = name
        self.description = description
        self.price = price
        if popularity is None:  # we don't use self here, because we're not actually assigning self.popularity on this line
            self.popularity = 0
        else:
            self.popularity = popularity

    def __str__(self):
        return self.name + ":\t$" + str(self.price)


test_product = Product("Test", "It's a test!", "1 bazillion dollars", 100)


print(test_product)
