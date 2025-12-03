class Event:
    def get_data(self):
        pass


class OrderEvent(Event):
    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data


class BaseTaskHandler:
    def process(self):
        pass


class SequentialTaskHandler:
    def __init__(self):
        self.next_task = None

    def process(self, event: Event):
        if self.next_task:
            self.next_task.process(event)
    
    def set_next(self, next_task: BaseTaskHandler) -> BaseTaskHandler:
        self.next_task = next_task
        return self.next_task


class ProductValidation(SequentialTaskHandler):
    def process(self, event: OrderEvent):
        print('Handle product validation such as product id, stock...', event.get_data())
        super().process(event)
    

class PlacingOrder(SequentialTaskHandler):
    def process(self, event: OrderEvent):
        print('Handle placing order', event.get_data())
        super().process(event)


class SendingEmail(SequentialTaskHandler):
    def process(self, event: OrderEvent):
        print('Handle sending email after placing order succesfully', event.get_data())
        super().process(event)


class PlacingOrderFacade:
    def process(cls, data):
        task_handler = SequentialTaskHandler()
        task_handler \
            .set_next(ProductValidation()) \
            .set_next(PlacingOrder()) \
            .set_next(SendingEmail())
        
        task_handler.process(data)


# Application will be run here
PlacingOrderFacade.process({
    'products': [
        {'id': 1, 'amount': 1},
        {'id': 2, 'amount': 1},
        {'id': 3, 'amount': 1}
    ]
})