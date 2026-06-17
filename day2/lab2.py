#exercise3
# Bank Account Balance Program

balance = float(input("Enter initial account balance: "))

while balance > 0:
    print("\nCurrent Balance:", balance)
    print("1. Deposit")
    print("2. Withdraw")

    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Deposit successful!")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient funds!")

    else:
        print("Invalid choice!")

print("\nAccount balance is zero.")
print("Program terminated.")