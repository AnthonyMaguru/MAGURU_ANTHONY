#exercise1
class MobileMoney:
    def __init__(self, balance):
        self.__balance = balance  # Private

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def check_balance(self):
        return self.__balance

account = MobileMoney(100000)  #Initial balance

account.deposit(50000)
account.withdraw(30000)

print("Current Balance:", account.check_balance())