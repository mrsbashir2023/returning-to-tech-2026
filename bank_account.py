# bank_account.py - Hebh Abed - Day 3 - C++ Class -> Python Class
# BCS 2007 OOP comeback

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        print(f"Account created for {self.owner} with ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit must be positive!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive!")
        elif amount > self.balance:
            print(f"Insufficient funds! You have ${self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Owner: {self.owner} | Balance: ${self.balance}")
        return self.balance

# This is like int main() in C++ - testing your class
if __name__ == "__main__":
    print("=== Bank Account OOP Demo ===")
    account1 = BankAccount("Hebh Abed", 100)
    account1.check_balance()
    account1.deposit(50)
    account1.withdraw(30)
    account1.withdraw(200)  # Should fail - testing edge case
    account1.check_balance()