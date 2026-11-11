# the entire test suite. yes, all of it.

from app import main


def test_subtotal():
    cart = {"tshirt": {"price": 299, "qty": 2}}
    assert main.subtotal(cart) == 598


def test_free_shipping_above_threshold():
    assert main.shipping(600) == 0


def test_percent_coupon_on_big_order():
    # 10% off a 1000 order, then 18% tax, free shipping: 1000 -> 900 -> 1062.0
    cart = {"hoodie": {"price": 1000, "qty": 1}}
    assert main.total(cart, {"type": "percent", "value": 10}) == 1062.0
