# Task 4: AI-Based Code Completion for Classes
# Prompt Used: "Generate a Python class Student with attributes (name, roll number, marks) and methods to calculate total and average marks."
class Student:
    def __init__(self, name: str, roll_number: int, marks: list):
        self.name = name
        self.roll_number = roll_number
        # Minor manual improvement: Validating that marks is a list
        self.marks = marks if isinstance(marks, list) else []

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

# Verification
student1 = Student("John Doe", 101, [85, 90, 78, 92])
print(f"Student: {student1.name}, Roll No: {student1.roll_number}")
print(f"Total Marks: {student1.calculate_total()}")
print(f"Average Marks: {student1.calculate_average()}")
# Verification: The class structure perfectly addresses the prompt by initializing the three requested attributes and providing the two distinct calculation methods.  
# Minor Manual Improvements & Justification: I added type hinting to the __init__ parameters (name: str, roll_number: int, marks: list) to improve code readability. I also added a conditional check inside calculate_average() to prevent a ZeroDivisionError in case an empty list of marks is passed, which makes the generated code more robust.  
