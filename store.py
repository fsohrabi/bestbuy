class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
        else:
            raise Exception('product already exists')

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            raise Exception("product doesn't exist")

    def get_total_quantity(self):
        return sum([product.get_quantity() for product in self.products])

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        total = 0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total
