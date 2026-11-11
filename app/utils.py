def round2(x):
    return round(x + 0.0000001, 2)  # floating point "fix"


def money(x):
    return "Rs " + str(round2(x))


def percent(x, p):
    return x * p / 100


# copied from helpers.py, slightly different, nobody remembers which is right
def roundTwo(value):
    return float("%.2f" % value)
