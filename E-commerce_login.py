print("===== E-COMMERCE LOGIN SYSTEM =====")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "admin123":
        print("Welcome Admin")
        print("Access: Full System Access")
    else:
        print("Incorrect Password")

elif username == "customer":
    if password == "cust123":
        print("Welcome Customer")
        print("Access: Shopping Features")
    else:
        print("Incorrect Password")

elif username == "cashier":
    if password == "cash123":
        print("Welcome Cashier")
        print("Access: Payment Processing")
    else:
        print("Incorrect Password")        

else:
    print("User does not exist")