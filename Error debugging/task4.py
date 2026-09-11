# Task 4: Calling a Non-Existent Method
# Bug Explanation: The code attempts to call my_car.drive(), but the drive method was never defined in the Car class, resulting in an AttributeError.
# Correction: Since the prompt implies the intention is to drive the car, the logical fix is to define the missing drive() method within the Car class
class Car:
    def start(self):
        return "Car started"
        
    # Defining the missing method
    def drive(self):
        return "Car is driving"

my_car = Car()

# 3 Assert Test Cases[cite: 1]
assert my_car.start() == "Car started"        # Confirm original method works
assert my_car.drive() == "Car is driving"     # Confirm new method works
assert hasattr(my_car, 'drive') == True       # Confirm the attribute now exists on the object