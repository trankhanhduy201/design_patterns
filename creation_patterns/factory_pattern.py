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

# Factory class to centralize creation of objects based on configuration
class PaymentFactory:
    def create_payment_method(self, type: str) -> PaymentMethod:
        if type == 'credit_card':
            return CreditCard()
        elif type == 'paypal':
            return Paypal()
        else:
            raise ValueError('Unknown payment method')
        
# Usage
factory = PaymentFactory()
credit_card = factory.create_payment_method('credit_card')
credit_card.pay()

paypal = factory.create_payment_method('paypal')
paypal.pay()