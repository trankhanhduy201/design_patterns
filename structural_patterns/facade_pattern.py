class Staff:
    def __init__(self, id: int, name: str, position: str):
        self.id = id
        self.name = name
        self.position = position

    def get_name(self):
        return self.name

class Waiter(Staff):
    def __init__(self, id: int, name: str):
        super().__init__(id, name, 'waiter')

class Chief(Staff):
    def __init__(self, id: int, name: str):
        super().__init__(id, name, 'chief')

class Order:
    def __init__(self, staff: Staff):
        if not type(staff) is Waiter:
            raise ValueError('Staff must be a waiter')
        self.products = []
        self.staff = staff
    
    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_products(self) -> list:
        return self.products if self.products else []

class Cooking:
    def __init__(self, staff: Staff, order: Order):
        self.staff = staff
        self.order = order

    def make_dishes(self):
        if not self.order or not self.staff:
            raise ValueError('Can not make dishes')
        
        for product in self.order.get_products():
            print(f'{self.staff.get_name()} is making {product}')

class Restaurent:
    @staticmethod
    def serve_customer(self):
        waiter = Waiter(id=1, name='Jimmy')
        order = Order(staff=waiter)
        chief = Chief(id=2, name='Alex')
        cooking = Cooking(staff=chief, order=order)
        cooking.make_dishes()

# Usage
Restaurent.serve_customer()