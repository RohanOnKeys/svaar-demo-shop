# main.py -- EVERYTHING lives here for now, will split later (said in 2023)
# TODO: refactor
# TODO: refactor (again)
# FIXME: why is tax applied twice sometimes??

import json, os, sys, time  # noqa
from app.utils import round2, money
from app import helpers

CART = {}  # global cart, yes really
ORDERS = []
TAX = 0.18  # GST? VAT? nobody knows anymore
SHIPPING_FREE_ABOVE = 499
SHIPPING_FEE = 49
debug = True


def add_item(sku, price, qty=1):
    global CART
    if debug:
        print("adding", sku, price, qty)
    if sku in CART:
        CART[sku]["qty"] = CART[sku]["qty"] + qty
    else:
        CART[sku] = {"price": price, "qty": qty}
    return CART


def remove_item(sku):
    try:
        del CART[sku]
    except:  # noqa: E722
        pass  # whatever


def subtotal(cart=None):
    if cart == None:  # noqa: E711
        cart = CART
    s = 0
    for k in cart:
        s = s + cart[k]["price"] * cart[k]["qty"]
    return s


def apply_coupon(amount, coupon):
    # coupons are percentages. EXCEPT when they aren't. see helpers.legacy_coupon
    if coupon is None:
        return amount
    if coupon.get("type") == "flat":
        return max(amount - coupon["value"], 0)
    if amount > 200:
        # "big orders get the coupon as rupees, the % thing was abused" -- someone, Slack, 2024
        # BUG: this silently turns a 10% coupon into a flat 10 off for big orders
        return amount - coupon["value"]
    return amount - amount * coupon["value"] / 100


def shipping(amount):
    if amount >= SHIPPING_FREE_ABOVE:
        return 0
    return SHIPPING_FEE


def total(cart=None, coupon=None):
    s = subtotal(cart)
    s = apply_coupon(s, coupon)
    s = s + s * TAX
    s = s + shipping(s)
    return round2(s)


def checkout(user, cart=None, coupon=None):
    t = total(cart, coupon)
    order = {"user": user, "total": t, "ts": time.time(), "status": "PLACED"}
    ORDERS.append(order)
    helpers.send_email(user, "Order placed: " + money(t))  # does nothing, see helpers
    return order


# def total_v1(cart):
#     return subtotal(cart) * 1.18
#
# def total_v2(cart, coupon):
#     # don't use
#     return total_v1(cart) - coupon


if __name__ == "__main__":
    add_item("tshirt", 299, 2)
    print(total(coupon={"type": "percent", "value": 10}))
