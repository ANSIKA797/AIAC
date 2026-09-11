# Task 1: AI-Based Code Completion for Loops
# Prompt Used: "Generate Python code to print all even numbers between 1 and N using a loop."
def print_even_numbers(n):
    # Loop from 1 to N (inclusive)
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, end=" ")

# Sample Input
n = 10
print(f"Even numbers between 1 and {n}:")
print_even_numbers(n)
# Loop Type Used: This implementation utilizes a for loop. A for loop is ideal here because the number of iterations (from 1 to N) is known beforehand.  Validation: For the sample input N = 10, the expected output will successfully validate the logic by printing 2 4 6 8 10.  