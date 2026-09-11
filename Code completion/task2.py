# Task 2: AI-Based Code Completion for Loop with Conditionals
# Prompt Used: "Generate Python code to count how many numbers in a list are even and odd."
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    return even_count, odd_count

# Validation
sample_list = [12, 7, 9, 24, 18, 5, 3]
evens, odds = count_even_odd(sample_list)
print(f"List: {sample_list}")
print(f"Even count: {evens}, Odd count: {odds}")
# Count Validation: Given the list [12, 7, 9, 24, 18, 5, 3], there are three even numbers (12, 24, 18) and four odd numbers (7, 9, 5, 3). The code correctly outputs Even count: 3, Odd count: 
# 4. Explanation of Logic Flow: The program initializes two counter variables at zero. It then iterates through each item in the list using a for loop. Inside the loop, an if conditional uses the modulo operator (%) to check if the remainder of the number divided by 2 is zero. If it is, the number is even, and the even_count increments. If not, the else block executes, incrementing the odd_count.  