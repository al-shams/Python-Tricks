# Bad Use Case: Unintentional Merging of Strings
# The missing comma causes "Dilbert" and "Jane" to merge into a single string.
names = [
    "Alice",
    "Bob",
    "Dilbert"  # <- Missing comma!
    "Jane",  # This merges with the previous line, resulting in "DilbertJane".
]
print(names)

# Good Use Case: Properly separated strings in the list
names = [
    "Alice",
    "Bob",
    "Dilbert",  # <- Correct comma placement
    "Jane",
]
print(names)

# Good Use Case: Cleaner Multi-Line Strings
# Here, the parentheses around the string allow it to be spread over multiple lines.
# No need for backslashes, making it cleaner and more readable.
my_str = (
    "This is a super long string constant "
    "spread out across multiple lines. "
    "And look, no backslash characters needed!"
)
print(my_str)

# Good Practice: Consistent trailing comma usage in collections
# Including a trailing comma helps with maintaining consistency
# and makes additions or reordering easier.
names = [
    "Alice",
    "Bob",
    "Dilbert",  # <- Trailing comma helps avoid mistakes when new elements are added
]
print(names)

# Smart formatting and comma placement can make your list, dict,
# or set constants easier to maintain.
# Python’s string literal concatenation feature can work to
# your benefit, or introduce hard-to-catch bugs.
