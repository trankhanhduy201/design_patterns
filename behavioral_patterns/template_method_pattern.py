from abc import ABC, abstractmethod

# Abstract tax
class Tax(ABC):
    @abstractmethod
    def get_rate(self, rate: float) -> float:
        pass

    def calculate(self, price):
        print('Calculate tax with rate')
        return price * self.get_rate()

'''
Concrete tax where can change the value of rate 
without modifying calculate function in parent class
'''
class NormalTax(Tax):
    def get_rate(self):
        print('Get rate for normal tax')
        return 0.1

class SpecialTax(Tax):
    def get_rate(self):
        print('Get rate for special tax')
        return 0.2
    
# Usage
total_price = 100

normal_tax = NormalTax()
result = normal_tax.calculate(total_price)

special_tax = SpecialTax()
result = special_tax.calculate(total_price)