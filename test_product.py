import pytest
from bestbuy.products import Product


def test_create_product():
    new_product = Product("Google Pixel 8", price=1450, quantity=100)
    assert isinstance(new_product, Product)


def test_create_product_without_name():
    with pytest.raises(ValueError, match="Invalid product creation parameters"):
        new_product = Product("", price=1450, quantity=100)


def test_create_product_wit_negative_price():
    with pytest.raises(ValueError, match="Invalid product creation parameters"):
        new_product = Product("MacBook Air M2", price=-10, quantity=100)


def test_create_product_wit_negative_quantity():
    with pytest.raises(ValueError, match="Invalid product creation parameters"):
        new_product = Product("MacBook Air M2", price=10, quantity=-100)


def test_reach_product_zero_quantity():
    new_product = Product("MacBook Air M2", price=10, quantity=100)
    new_product.set_quantity(0)
    assert not new_product.is_active()


def test_purchase_product_modify_quantity():
    new_product = Product("MacBook Air M2", price=10, quantity=100)
    new_product.buy(5)
    assert new_product.get_quantity() == 95


def test_buying_product_wit_larger_quantity():
    with pytest.raises(ValueError, match="Insufficient stock available"):
        new_product = Product("MacBook Air M2", price=10, quantity=100)
        new_product.buy(105)
