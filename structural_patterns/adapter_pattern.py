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

# New abstract payment method
class BankTransfer(ABC):
    @abstractmethod
    def transfer(self): pass

# New concrete payment method
class Vietcombank(BankTransfer):
    def transfer(self):
        print('Pay by transferring')

# A bank transfer adapter to make the new payment method compatible with the current payment system
class BankTransferAdapter(PaymentMethod):
    def __init__(self, bank_transfer: BankTransfer):
        self.bank_transfer = bank_transfer

    def pay(self):
        self.bank_transfer.transfer()

# Order class
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

# Now change to new payment method with different interface
bank_transfer = BankTransferAdapter()
order = Order(bank_transfer)
order.place_order()