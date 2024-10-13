def calculate_price(product, discount):
    return int(product["price"] * (1.0 - discount))


def apply_discount_with_assert(product, discount):
    assert 0 <= discount <= 1, f"Discount must be between 0 and 1. it is '{discount}'."
    return calculate_price(product, discount)


def apply_discount_with_exception(product, discount):
    if 0 <= discount <= 1:
        return calculate_price(product, discount)
    else:
        raise ValueError(f"Discounted price is out of valid range. it is '{discount}'.")


if __name__ == "__main__":
    shoes = {
        "name": "Fancy Shoes",
        "price": 14900,
    }
    discount = 2

    price = apply_discount_with_assert(shoes, discount)
    print(price)

    price = apply_discount_with_exception(shoes, discount)
    print(price)

# At its core, Python’s assert statement is a debugging aid that tests a
# condition. If the assert condition is true, nothing happens, and your
# program continues to execute as normal. But if the condition evaluates to false,
# an AssertionError exception is raised with an optional
# error message.
