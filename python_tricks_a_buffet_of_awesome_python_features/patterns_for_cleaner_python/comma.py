# Bad Use Case: Unintentional Merging of Strings
names = [
    "Alice",
    "Bob",
    "Dilbert"  # <- Missing comma!
    "Jane",
]
print(names)

# Good Use Case: Cleaner Multi-Line Strings
my_str = (
    "This is a super long string constant "
    "spread out across multiple lines. "
    "And look, no backslash characters needed!"
)
print(my_str)

# Consistent Comma Usage in Collections
names = [
    "Alice",
    "Bob",
    "Dilbert",
]
print(names)

# Smart formatting and comma placement can make your list, dict,
# or set constants easier to maintain.
# Python’s string literal concatenation feature can work to
# your benefit, or introduce hard-to-catch bugs.
