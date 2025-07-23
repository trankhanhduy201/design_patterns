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

class Log(ABC):
    @abstractmethod
    def write(self, message: str): pass

# Concrete logging
class LogFile(Log):
    def write(self, message: str):
        print('Log file: ' + message)

'''
Decorator class is to add more behaviors or responsibilities
without modifying existing codes
'''
class PaymentMethodLogging(PaymentMethod):
    def __init__(self, payment_method: PaymentMethod, log: Log):
        self.payment_method = payment_method
        self.log = log
    
    def pay(self):
        self.log.write('Pre payment')
        self.payment_method.pay()

# Usage
credit_card = CreditCard()
log = LogFile()
payment_decorator = PaymentMethodLogging(credit_card, log)
payment_decorator.pay()
        