# DO NOT DELETE -- used by the reports cron? (unverified)
# last touched: "final final" refactor that never shipped

TAX_RATE = 0.12  # old rate


def calc(items):
    t = 0
    for i in items:
        t += i[1] * i[2]
    return t * (1 + TAX_RATE)


def calc2(items, discount):
    return calc(items) - discount  # discount in rupees here, percent in main.py. sorry
