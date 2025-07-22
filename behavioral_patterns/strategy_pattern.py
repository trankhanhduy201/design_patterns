from abc import ABC, abstractmethod

# Abstract tax
class Tax(ABC):
    @abstractmethod
    def calculate(self, price): pass

# Concrete Tax
class NormalTax(Tax):
    def calculate(self, price: float) -> float:
        print('Calculate normal tax')
        return price * 0.1

class SpecialTax(Tax):
    def calculate(self, price: float) -> float:
        print('Calculate special tax')
        return price * 0.2

# Product class have multiple tax, and can switch between them at runtime
class Product:
    def __init__(self):
        self.price = 100

    def set_tax(self, tax: Tax):
        self.tax = tax

    def total_price(self) -> float:
        return self.price + self.tax.calculate(self.price)
        
        
# Usage
product = Product()

# Switch tax
product.set_tax(NormalTax())
total_price = product.total_price()

product.set_tax(SpecialTax())
total_price = product.total_price()
