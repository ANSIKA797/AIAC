history = []

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Show History")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "6":
        print("Thank you!")
        break

    elif choice == "5":
        print("Calculation History:")
        for item in history:
            print(item)

    elif choice in ["1", "2", "3", "4"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            result = a + b
            symbol = "+"

        elif choice == "2":
            result = a - b
            symbol = "-"

        elif choice == "3":
            result = a * b
            symbol = "*"

        else:
            if b == 0:
                print("Cannot divide by zero")
                continue
            result = a / b
            symbol = "/"

        print("Result =", result)

        history.append(f"{a} {symbol} {b} = {result}")

    else:
        print("Invalid choice!")

# Output:
# Enter choice: 1
# Enter first number: 10
# Enter second number: 5
# Result = 15.0
#
# Enter choice: 3
# Enter first number: 4
# Enter second number: 3
# Result = 12.0
#
# Enter choice: 5
# Calculation History:
# 10.0 + 5.0 = 15.0
# 4.0 * 3.0 = 12.0
#
# Enter choice: 6
# Thank you!