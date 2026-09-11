# Task 3: AI-Based Code Completion for Class Attributes ValidationPrompt Used: "Generate a Python class User that validates age and email using conditional statements."  
class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = self.validate_age(age)
        self.email = self.validate_email(email)

    def validate_age(self, age):
        if isinstance(age, int) and age > 0:
            return age
        else:
            return "Invalid Age"

    def validate_email(self, email):
        if "@" in email and "." in email:
            return email
        else:
            return "Invalid Email"

# Test cases for valid and invalid inputs
user1 = User("Alice", 20, "alice@example.com")
print(f"User 1: {user1.name}, {user1.age}, {user1.email}")

user2 = User("Bob", -5, "bobatexample.com")
print(f"User 2: {user2.name}, {user2.age}, {user2.email}")
# Verification of Condition Handling: The validate_age method successfully uses a conditional to ensure the age is a positive integer. The validate_email method uses conditionals to check for the presence of basic email characteristics (the @ and . symbols).  
# Test Cases: user1 represents a valid input and successfully assigns all attributes. user2 tests the invalid inputs (negative age, missing '@' in email), which triggers the conditionals to assign the error strings instead.
