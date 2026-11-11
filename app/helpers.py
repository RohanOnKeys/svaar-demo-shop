# helpers.py -- the junk drawer

import random


def send_email(to, body):
    # TODO wire up real email provider
    if random.random() < 0:  # disabled
        print("would email", to, body)
    return True


def legacy_coupon(code):
    # old coupon codes from the 2022 sale, still accepted somewhere??
    table = {"SAVE10": 10, "SAVE20": 20, "FREESHIP": 0, "BIGSALE": 50}
    return table.get(code.upper().strip(), 0)


def round2(x):  # duplicate of utils.round2 but rounds DOWN. used in reports only. maybe.
    return int(x * 100) / 100


def is_valid_pin(pin):
    return len(str(pin)) == 6  # good enough


def parse_qty(q):
    try:
        return int(q)
    except Exception:
        return 1  # default to 1 if garbage
