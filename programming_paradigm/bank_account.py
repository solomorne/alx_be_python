"""Defining a class named BankAccount"""
class BankAccount:
    """Initialize an account balance"""
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        """Add specified amount to balance."""
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        """Deduct specified amount if funds are sufficient.
        Returns True if successful, False if not."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current balance in a user-friendl format."""
        print(f"Your current balance is: ${self._balance:.2f}")
