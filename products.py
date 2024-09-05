class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise Exception('Somthing is wrong in creating product')
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity == 0:
            self.deactivate()
        else:
            self.activate()
        self.quantity = quantity

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if self.quantity < quantity:
            raise Exception(f"There isn't enough {self.name}")
        self.set_quantity(self.quantity - quantity)
        return quantity * self.price

