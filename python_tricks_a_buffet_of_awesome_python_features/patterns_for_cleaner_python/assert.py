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


def apply_discount_with_debug(product, discount):
    expression1 = 0 <= discount <= 1
    expression2 = f"Discounted price is out of valid range. it is '{discount}'."
    if __debug__:
        if not expression1:
            raise AssertionError(expression2)
        return calculate_price(product, discount)


if __name__ == "__main__":
    shoes = {
        "name": "Fancy Shoes",
        "price": 14900,
    }
    discount = 0.5

    price = apply_discount_with_assert(shoes, discount)
    print(price)

    price = apply_discount_with_exception(shoes, discount)
    print(price)

    price = apply_discount_with_debug(shoes, discount)
    print(price)

# At its core, Python’s assert statement is a debugging aid that tests a
# condition. If the assert condition is true, nothing happens, and your
# program continues to execute as normal. But if the condition evaluates to false,
# an AssertionError exception is raised with an optional error message.

# Assertions inform developers about unrecoverable errors in a program.
# They do not signal expected error conditions, like File-Not-Found errors.
# Users can take corrective actions for expected error conditions.
# Users can attempt to try again after encountering an error.
# These situations differ from unrecoverable errors identified by assertions.
# Assertions serve as internal self-checks within the code.
# They declare certain conditions as impossible; a failure indicates a bug.
# When an assertion fails, the program crashes with a specific assertion error message.
# Assertions help track down and fix bugs more easily.
# The assert statement is a debugging aid, not for handling run-time errors.
# An assertion error should indicate a bug in the program.
# Assertions help developers quickly identify the likely root cause of bugs.

# Use regular if statements for data validation instead of assertions,
# as assertions can be globally disabled with an interpreter setting (-O and -OO flags).
# Avoid using non-empty tuples in assert statements, as they always
# evaluate to true in Python, causing the assertion to never fail.
