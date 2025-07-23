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

# Proxy class provides the substitute object that manage access to real object
class PaymentProxy(PaymentMethod):
    def __init__(self, user_type: str):
        self.user_type = user_type

    def pay(self):
        if not self.payment_method:
            if self.user_type == 'normal':
                self.payment_method = CreditCard()
            elif self.user_type == 'vip':
                self.payment_method = Paypal()
        self.payment_method.pay()

# Usage
payment_proxy = PaymentProxy(user_type='vip')
payment_proxy.pay()

        