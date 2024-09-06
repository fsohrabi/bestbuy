import pytest

import promotions
from products import Product, NonStockedProduct, LimitedProduct


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


def test_create_non_stocked_product():
    new_product = NonStockedProduct("Windows License", price=250)
    assert isinstance(new_product, NonStockedProduct)


def test_create_limited_product():
    new_product = LimitedProduct("shipping", price=250, maximum=1, quantity=100)
    assert isinstance(new_product, LimitedProduct)


def test_create_product_with_promotion():
    new_product = Product("MacBook Air M2", price=10, quantity=100)
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    new_product.promotion = third_one_free
    assert new_product.promotion.name == "Third One Free!"


def test_reach_product_zero_quantity():
    new_product = Product("MacBook Air M2", price=10, quantity=100)
    new_product.quantity = 0
    assert not new_product.is_active()


def test_purchase_product_modify_quantity():
    new_product = Product("MacBook Air M2", price=10, quantity=100)
    new_product.buy(5)
    assert new_product.quantity == 95


def test_buying_product_wit_larger_quantity():
    with pytest.raises(ValueError, match="Insufficient stock available"):
        new_product = Product("MacBook Air M2", price=10, quantity=100)
        new_product.buy(105)


def test_buying_product_wit_second_half_price_promotion():
    new_product = Product("MacBook Air M2", price=100, quantity=100)
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    new_product.promotion = second_half_price
    assert new_product.buy(2) == 150


def test_buying_product_wit_third_one_free_promotion():
    new_product = Product("MacBook Air M2", price=100, quantity=100)
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    new_product.promotion = third_one_free
    assert new_product.buy(3) == 200


def test_buying_product_wit_thirty_percent_promotion():
    new_product = Product("MacBook Air M2", price=100, quantity=100)
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)
    new_product.promotion = thirty_percent
    assert new_product.buy(2) == 140


def test_buying_product_limited_product():
    with pytest.raises(ValueError, match="Error while making order! Only 1 is allowed from this shipping!"):
        new_product = LimitedProduct("shipping", price=10, quantity=100, maximum=1)
        new_product.buy(5)
