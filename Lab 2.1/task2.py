def is_armstrong_gemini(num):
    """
    Checks if a number is an Armstrong number using string conversion.
    """
    if num < 0:
        return False

    # Convert number to string to easily iterate digits and find length
    digits = str(num)
    power = len(digits)

    # Calculate sum of each digit raised to the power of total digits
    armstrong_sum = sum(int(digit) ** power for digit in digits)

    return armstrong_sum == num

# Sample test cases
for n in [153, 9474, 123]:
    print(f"{n} is Armstrong: {is_armstrong_gemini(n)}")
    #OUTPUT:
    #153 is Armstrong: True
    #9474 is Armstrong: True
    #123 is Armstrong: False