# shop-api (demo)

> **This repository is deliberately messy.** It exists only so Svaar has a real,
> failing CI pipeline to watch during demos. Nothing here is deployed, there are no
> real credentials, and none of this code should be copied anywhere.

Tiny order/checkout logic for an imaginary online shop. It grew "organically":
duplicated helpers, a god module, dead files, magic numbers and almost no tests.

## Run the tests

```
pip install -r requirements.txt
pytest
```

One test fails on `main` on purpose: there is a real bug in how percentage coupons
are applied to large orders. CI goes red, Svaar notices, and the demo begins.

## Workflows

- `ci.yml` runs the (few) tests on every push and can be started by hand.
- `svaar-demo.yml` is Svaar's controlled demo workflow: started by hand only, it
  fails when `fail=true` and succeeds otherwise. It never deploys anything.
