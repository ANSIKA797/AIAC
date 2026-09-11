# Task 3: Runtime Error - File Not FoundBug Explanation: Attempting to open a file that does not exist without proper error handling will crash the program with a FileNotFoundError.  Correction: Wrap the file opening operation in a try-except block to gracefully catch the error and return a user-friendly message instead of crashing the program.  
import os

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."
    except OSError:
        return "Error: Invalid path or OS error encountered."

# Setup for testing scenario 1 (file exists)
with open("test_exists.txt", "w") as f:
    f.write("Lab 7 Success")

# 3 Assert Test Cases matching the required scenarios
assert read_file("test_exists.txt") == "Lab 7 Success" # Scenario 1: File exists
assert "not found" in read_file("nonexistent.txt")     # Scenario 2: File missing[cite: 1]
assert "Error:" in read_file("///invalid***path///")   # Scenario 3: Invalid path[cite: 1]

# Cleanup test file
os.remove("test_exists.txt")
