class Product:
    """
    Represents a product in the store.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The available quantity of the product.
        active (bool): Whether the product is active and available for sale.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a Product object.

        Args:
            name (str): The product name.
            price (float): The product price. Must be non-negative.
            quantity (int): The available product quantity. Must be non-negative.

        Raises:
            ValueError: If price or quantity is negative, or if name is empty.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError('Invalid product creation parameters')
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity of the product.

        If quantity is set to 0, the product is deactivated.
        If quantity is positive, the product is activated.

        Args:
            quantity (int): The new product quantity.
        """
        if quantity == 0:
            self.deactivate()
        else:
            self.activate()
        self.quantity = quantity

    def is_active(self):
        """Returns whether the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def __str__(self):
        """
        Displays the product information in a readable format.

        Returns:
            str: The formatted product details.
        """
        return f"{self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """
        Processes the purchase of the product.

        Args:
            quantity (int): The amount of the product to buy.

        Returns:
            float: The total price for the purchased products.

        Raises:
            ValueError: If the requested quantity exceeds available stock.
        """
        if self.quantity < quantity:
            raise ValueError("Insufficient stock available")
        self.set_quantity(self.quantity - quantity)
        return quantity * self.price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def __str__(self):
        """
        Displays the product information in a readable format.

        Returns:
            str: The formatted product details.
        """
        return f"{self.name}, Price: ${self.price:.2f}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def __str__(self):
        """
        Displays the product information in a readable format.

        Returns:
            str: The formatted product details.
        """
        return f"{self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}, Maximum: {self.maximum}"
