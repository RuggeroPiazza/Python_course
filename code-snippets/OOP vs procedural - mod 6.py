'''
Use case: bank system.
In the procedural approach, you might represent a banking system using functions that operates
on data structures.
In the OOP approach, you can model the system using classes to represent entities like 'account'
and encapsulate related data and behaviors within those classes.
'''
# procedural
def create_account(account_holder, initial_balance):
    # Logic to create a new bank account
    pass

def deposit(account, amount):
    # Logic to deposit money into an account
    pass

def withdraw(account, amount):
    # Logic to withdraw money from an account
    pass

# Usage
account1 = create_account("John Doe", 1000)
deposit(account1, 500)
withdraw(account1, 200)

# OOP
# each account is represented as an object with its own data and methods
# This makes the code more modular, encapsulated, and easier to understand.
class Account:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

# Usage
account1 = Account("John Doe", 1000)
account1.deposit(500)
account1.withdraw(200)
