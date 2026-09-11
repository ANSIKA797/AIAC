# Task 2: Incorrect condition in an If StatementBug Explanation: The original code uses a single equals sign (=) inside the if statement (if n = 10:). In Python, = is the assignment operator used to assign values to variables. To check for equality, you must use the comparison operator ==. Using = in a condition causes a SyntaxError.  Correction: Change = to ==.  
def check_number(n):
    if n == 10:
        return "Ten"
    else:
        return "Not Ten"

# 3 Assert Test Cases
assert check_number(10) == "Ten"     # Test with the exact target number
assert check_number(5) == "Not Ten"  # Test with a smaller number
assert check_number(-10) == "Not Ten" # Test with a negative number
