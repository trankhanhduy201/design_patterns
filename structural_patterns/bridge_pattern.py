from abc import ABC, abstractmethod

# Abstract payment method
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self): pass

# Concrete payment method
class CreditCard(PaymentMethod):
    def pay(self):
        print('Pay by credit card')

class Paypal(PaymentMethod):
    def pay(self):
        print('Pay by paypal')

'''
Decoupling abstraction and implementations by injecting instance into constructor method,
and making implementations can vary independently
'''
class Order:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def get_total_price(self) -> float:
        return 1000
        
    def place_order(self):
        print('Place order is taking place')
        total_price = self.get_total_price()
        self.payment_method.pay(total_price)
        
# Usage
credit_card = CreditCard()
order = Order(credit_card)
order.place_order()

paypal = Paypal()
order = Order(paypal)
order.place_order()