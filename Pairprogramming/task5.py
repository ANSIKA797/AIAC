# Original buggy code
a = 10
b = 0

# print(a / b)
# Error: ZeroDivisionError

# Corrected code
a = 10
b = 0

if b != 0:
    print("Result =", a / b)
else:
    print("Cannot divide by zero")

# Output:
# Cannot divide by zero