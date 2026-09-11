# Task 5: TypeError - Mixing Strings and Integers in Addition
# Bug Explanation: The original code attempts to add a string ("10") and an integer (5). Python is a strongly typed language and does not implicitly convert these types for addition, resulting in a TypeError[cite: 1].
# Correction: As requested, here are two solutions: Type casting (converting the string to an integer for mathematical addition) and String concatenation (converting the integer to a string to join them)
# Solution A: Type Casting (Mathematical Addition)[cite: 1]
def add_five_math(value):
    return int(value) + 5

# Solution B: String Concatenation[cite: 1]
def add_five_concat(value):
    return str(value) + "5"

# 3 Assert Test Cases (Validating multiple inputs)[cite: 1]
assert add_five_math("10") == 15     # String input mathematically added
assert add_five_math(10) == 15       # Integer input mathematically added
assert add_five_concat("10") == "105" # String input concatenated