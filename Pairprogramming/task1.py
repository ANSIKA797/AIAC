tasks = []

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("Your Tasks:")
        for task in tasks:
            print("-", task)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

# Output:
# 1. Add Task
# 2. Show Tasks
# 3. Exit
# Enter choice: 1
# Enter task: Complete lab work
# Task added!
#
# Enter choice: 2
# Your Tasks:
# - Complete lab work
#
# Enter choice: 3
# Goodbye!