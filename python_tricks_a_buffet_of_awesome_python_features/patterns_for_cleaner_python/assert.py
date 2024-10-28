def calculate_discounted_price(product_info, discount_rate):
    """Calculates the price after applying a discount to the product."""
    return int(product_info["price"] * (1.0 - discount_rate))


def apply_discount_with_assertion(product_info, discount_rate):
    """Applies a discount and uses an assertion to validate the discount rate."""
    is_discount_valid = 0 <= discount_rate <= 1
    assert (
        is_discount_valid
    ), f"Discount must be between 0 and 1. It is '{discount_rate}'."
    return calculate_discounted_price(product_info, discount_rate)


def apply_discount_with_error_handling(product_info, discount_rate):
    """Applies a discount and raises a ValueError if the discount rate is invalid."""
    is_discount_valid = 0 <= discount_rate <= 1
    if is_discount_valid:
        return calculate_discounted_price(product_info, discount_rate)
    else:
        raise ValueError(f"Discount must be between 0 and 1. It is '{discount_rate}'.")


def apply_discount_with_debug_check(product_info, discount_rate):
    """Applies a discount with a debug check for invalid discount rates."""
    is_discount_valid = 0 <= discount_rate <= 1
    error_message = f"Discount must be between 0 and 1. It is '{discount_rate}'."
    if __debug__:
        if not is_discount_valid:
            raise AssertionError(error_message)
    return calculate_discounted_price(product_info, discount_rate)


if __name__ == "__main__":
    product_example = {
        "name": "Fancy Shoes",
        "price": 14900,
    }
    discount_rate = 0.5

    final_price = apply_discount_with_assertion(product_example, discount_rate)
    print(final_price)

    final_price = apply_discount_with_error_handling(product_example, discount_rate)
    print(final_price)

    final_price = apply_discount_with_debug_check(product_example, discount_rate)
    print(final_price)

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
