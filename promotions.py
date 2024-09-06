from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        """
        For every two items, the second one is half price.

        Args:
            product (Product): The product object.
            quantity (int): The quantity being purchased.

        Returns:
            float: The total price after applying the promotion.
        """
        # Calculate how many full-price items and half-price items there are.
        half_price_count = quantity // 2
        full_price_count = quantity - half_price_count

        # Compute total cost
        total_price = (full_price_count * product.price) + (half_price_count * product.price * 0.5)
        return total_price


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        """
        For every three items, one is free.

        Args:
            product (Product): The product object.
            quantity (int): The quantity being purchased.

        Returns:
            float: The total price after applying the promotion.
        """
        # Calculate how many paid items and free items there are.
        free_items = quantity // 3
        paid_items = quantity - free_items

        # Compute total cost
        total_price = paid_items * product.price
        return total_price


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """
        Apply a percentage discount on the total price.

        Args:
            product (Product): The product object.
            quantity (int): The quantity being purchased.

        Returns:
            float: The total price after applying the discount.
        """
        # Calculate total price and apply the discount
        total_price = product.price * quantity
        discount = total_price * (self.percent / 100)
        return total_price - discount

