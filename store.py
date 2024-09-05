class Store:
    """
    Represents a store containing multiple products.

    Attributes:
        products (list): A list of Product objects available in the store.
    """

    def __init__(self, products=None):
        """
        Initializes a Store object.

        Args:
            products (list, optional): A list of Product objects to add to the store.
            Defaults to an empty list.
        """
        self.products = products if products else []

    def add_product(self, product):
        """
        Adds a product to the store.

        Args:
            product (Product): The product to add.

        Raises:
            ValueError: If the product already exists in the store.
        """
        if product not in self.products:
            self.products.append(product)
        else:
            raise ValueError('Product already exists in the store')

    def remove_product(self, product):
        """
        Removes a product from the store.

        Args:
            product (Product): The product to remove.

        Raises:
            ValueError: If the product is not found in the store.
        """
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product doesn't exist in the store")

    def get_total_quantity(self):
        """
        Returns the total quantity of all products in the store.

        Returns:
            int: Total quantity of all active products.
        """
        return sum(product.get_quantity() for product in self.products if product.is_active())

    def get_all_products(self):
        """
        Returns all active products in the store.

        Returns:
            list: A list of active Product objects.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """
        Processes an order from the store.

        Args:
            shopping_list (list): A list of tuples, each containing a
            Product object and the quantity to buy.

        Returns:
            float: The total cost of the order.

        Raises:
            ValueError: If any product's requested quantity is greater than available stock.
        """
        total = 0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total
