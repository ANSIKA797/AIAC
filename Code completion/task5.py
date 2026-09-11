# Task 5: AI-Assisted Code Completion Review
# Prompt Used: "Generate a Python program for a simple bank account system using class, loops, and conditional statements."
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Insufficient funds or invalid amount.")

def main():
    account = BankAccount("Adagiri", 100)
    
    while True:
        print("\n--- Bank Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            print("Thank you for using the bank system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Uncomment the line below to run the interactive program
    # main()
    pass
    # Complete Output: The program combines a class (BankAccount), a while True loop to keep the interactive menu running, and conditional statements (if/elif/else) to handle user choices and validate transaction amounts.
    # Strengths and Limitations: A key strength of AI suggestions is the rapid generation of structural boilerplate (like class definitions and standard while loops for menus) with syntactically correct code. A limitation is that the AI might not immediately anticipate complex real-world edge cases (e.g., handling ValueError if the user types a string when asked for a deposit amount) unless explicitly prompted to handle exceptions.  
    # Reflection on Productivity: AI dramatically boosts productivity by taking care of repetitive typing and basic logic structuring. This allows you to focus on the higher-level logic, user experience, and refining edge cases rather than worrying about exact syntax.  
    