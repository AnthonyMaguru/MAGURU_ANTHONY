#Polymorphism 
# What is Polymorphism?
#Polymorphism means "many forms". 
#In programming, polymorphism allows methods to do different things 
# based on the object it is acting upon.

# Why Polymorphism?
#code reusability, flexibility, and maintainability. 
#It allows for a single interface to represent different underlying forms (data types).



#method overloading
#what is method overloading?
#Method overloading is a concept in object-oriented programming where
# multiple methods can have the same name but different parameters.

#in python
#Approach 1: Using default parameters
#class Calculator:
#    def add(self, a, b):
#        return a + b

#    def add(self, a, b, c):
#        return a + b + c

#calc = Calculator()
#print(calc.add(2, 3, 4))

#Approach 2: Using variable length arguments
class Calculator:
    def add(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        
        elif len(args) == 3:
            return args[0] + args[1] + args[3]
        elif len(args) > 3:
            return sum(args)
        else:
            return 0
        
#Approach 3: Using type checking

"""class Calculator:
    if isinstance(a, int) and isinstance(b, int):
        return a + b
        
    elif isinstance(a, float) and isinstance(b, float):
        return float(a) + float(b)
    elif isinstance(a, str) and isinstance(b, str):
        return str(a) + str(b)
        
        """
        
#method overriding
#What is method overriding?
#Method overriding is a feature in object oriented programming 
#where a subclass provides a specific implementation of a

#key points
"""
-the method signature (name and parameters) mus match
- super() allow calling the parent method
- Overriding enable dynamic behaviours at return
"""

        
#Real world Example: Bank Account
class BankAccount:
    def calculate_interest(self, principal, rate, time):
        return (principal * rate * time) / 100
    def get_accout_type(self):
        return "Generic Bank Account"
    
class SavingAccount(BankAccount):
    def calculate_interest(self, principal, rate):
        monthly_rate = rate / 12 /100
        return balance * ((1+ monthly_rate)**12 - 1)
    
    def get_accout_type(self):
        return "Saving Account"
    
class CheckingAccount(BankAccount):
    def calculate_interest(self, balance, rate):
        #Checking Account
        return 0
    
    def get_account_type(self):
        return "Checking Account"
    
# Lab 1 Exercise 1: Create a method overloading and overriding the completes a banking system
# The parent class must be Transaction and the child class can be deposit, withdrwal and Transfer.
# Demonstrate an employer dpositing, witdrawing and transfering funds.

class Transaction:
    def __init__(self, amount):
        self.amount = amount

    def execute(self):
        print(f"Executing base transaction of ${self.amount}")

    def execute(self, note="No note provided"):
        print(f"Transaction of ${self.amount} - Note: {note}")

class Deposit(Transaction):
    def execute(self, note="Deposit"):
        print(f"Depositing ${self.amount}. {note}")

class Withdrawal(Transaction):
    def execute(self, note="Withdrawal"):
        print(f"Withdrawing ${self.amount}. {note}")

class Transfer(Transaction):
    def execute(self, note="Transfer"):
        print(f"Transferring ${self.amount}. {note}")

# Demonstrating the banking system
print("--- Employer Banking Actions ---")

emp_deposit = Deposit(5000)
emp_deposit.execute("Salary Deposit")

emp_withdraw = Withdrawal(200)
emp_withdraw.execute("ATM Withdrawal")

emp_transfer = Transfer(1000)
emp_transfer.execute("Rent Payment")

#operator overloading
#What is operator overloading?
#Operator overloading is a feature in object oriented programming that 
#allows developers to redefine the behavior of operators (like +, -, *, /) for user defined types (classes).
"""
- Add +, Substract -, Mulitpy *, Division / 

Common Special Methods:
__add__(self, other)
__sub__(self,other)
__mul__(self, other)
__truediv__(self, other)
__str__(self,other)

"""
#Example3
class money:
    def __init__(self, amount, currency='UGX'):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError('Cannot add different currencies')
        return money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        pass
    def __mul__(self, other):
        pass

# Automation and webscrapping
#What is automation in python?
#Automation in Python refers to the process of using Python 
#scripts and libraries to perform repetitive tasks,

"""
The Automation Pipeline:

Input -> , Transform -> , Output -> , Reliability -> Run


# Key Libraries for Auomation
Library 
pathlib - file path
shutil - copy , move, archive
Schedule - task Schduling
Watchdog  - File System events monitoring
openpyxl - Excel file read / write

"""

#Example 4/ File Automation
#File Automation 
#organising files on our computer based on their extensions or types can be a tedious task.


