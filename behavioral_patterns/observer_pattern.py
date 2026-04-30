from abc import ABC, abstractmethod

class Event:
    pass

class StockEvent(Event):
    def __init__(self, old_price, new_price):
        self.old_price = old_price
        self.new_price = new_price

class Observer(ABC):
    @abstractmethod
    def update(self, event: Event):
        pass

class Publisher:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, event: Event):
        for observer in self._observers:
            observer.update(event)

class Stock(Publisher):
    def __init__(self, price=0):
        super().__init__()
        self.price = price

    def update_price(self, price):
        if self.price == price:
            return

        old_price = self.price
        self.price = price
        self.notify(StockEvent(old_price, price))

class MobileApp(Observer):
    def update(self, event: Event):
        if isinstance(event, StockEvent):
            print(f"📱 Mobile App: Price changed from {event.old_price} to {event.new_price}")

class WebApp(Observer):
    def update(self, event: Event):
        if isinstance(event, StockEvent):
            print(f"💻 Web App: Price changed from {event.old_price} to {event.new_price}")


stock = Stock()
stock.add_observer(MobileApp())
stock.add_observer(WebApp())
stock.update_price(100)
stock.update_price(120)