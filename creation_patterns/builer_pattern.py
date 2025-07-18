class Pizza:
    def __init__(self, size, cheese=False, pepperoni=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni

    def __str__(self):
        return f"Pizza(size={self.size}, cheese={self.cheese}, pepperoni={self.pepperoni})"

# Builder class to hide the complexity of creation logic
class PizzaBuilder:
    def __init__(self, size):
        self.size = size
        self.cheese = False
        self.pepperoni = False

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def build(self) -> Pizza:
        return Pizza(self.size, self.cheese, self.pepperoni)
    
# Usage
builder = PizzaBuilder()
builder.add_cheese().add_pepperoni().build()