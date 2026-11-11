STOCK = {"tshirt": 12, "mug": 0, "hoodie": 3, "sticker": 999}


def in_stock(sku, qty=1):
    return STOCK.get(sku, 0) >= qty


def reserve(sku, qty=1):
    # race condition city, but it's fine, we have like 4 users
    if in_stock(sku, qty):
        STOCK[sku] -= qty
        return True
    return False


def restock(sku, qty):
    STOCK[sku] = STOCK.get(sku, 0) + qty
