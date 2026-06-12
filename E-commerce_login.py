print("====================================")
print("     E-COMMERCE MANAGEMENT SYSTEM")
print("====================================")

# LOGIN SECTION
username = input("Enter Username: ")
password = input("Enter Password: ")

logged_in = False
role = ""

# Authentication
if username == "admin":
    if password == "admin123":
        logged_in = True
        role = "Admin"
    else:
        print("Incorrect Password")

elif username == "customer":
    if password == "cust123":
        logged_in = True
        role = "Customer"
    else:
        print("Incorrect Password")

elif username == "cashier":
    if password == "cash123":
        logged_in = True
        role = "Cashier"
    else:
        print("Incorrect Password")

else:
    print("User does not exist")

# SYSTEM ACCESS
if logged_in:

    print("\nLogin Successful!")
    print("Logged in as:", role)

    # ADMIN MENU
    if role == "Admin":

        print("\n===== ADMIN MENU =====")
        print("1. Manage Products")
        print("2. Manage Users")
        print("3. View Sales Reports")
        print("4. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            print("Opening Product Management Module...")

        elif choice == 2:
            print("Opening User Management Module...")

        elif choice == 3:
            print("Opening Sales Reports Module...")

        elif choice == 4:
            print("Goodbye!")

        else:
            print("Invalid Option")

    # CUSTOMER MENU
    elif role == "Customer":

        print("\n===== CUSTOMER MENU =====")
        print("1. Browse Products")
        print("2. Place Order")
        print("3. View Order History")

        choice = int(input("Choose an option: "))

        if choice == 1:
            print("Displaying Products...")

        elif choice == 2:

            print("\n===== CHECKOUT =====")

            subtotal = float(input("Enter Product Subtotal: "))
            coupon = input("Enter Coupon Code: ")

            tax_countries = {
                "1": ("Uganda", 0.18),
                "2": ("Kenya", 0.16),
                "3": ("Tanzania", 0.18),
                "4": ("Other", 0.10),
            }

            print("\nSelect country for tax:")
            for number, (country, rate) in tax_countries.items():
                print(f"{number}. {country}")

            country_choice = input("Enter the number corresponding to the country: ")
            location, tax_rate = tax_countries.get(country_choice, ("Other", 0.10))

            # Discount based on subtotal
            if subtotal >= 500000:
                discount = subtotal * 0.20
            elif subtotal >= 200000:
                discount = subtotal * 0.10
            else:
                discount = subtotal * 0.05

            # Coupon validation
            if coupon == "SAVE10":
                coupon_discount = subtotal * 0.10

            elif coupon == "SAVE20":
                coupon_discount = subtotal * 0.20

            else:
                coupon_discount = 0
                print("Invalid Coupon Code")

            total_discount = discount + coupon_discount

            amount_after_discount = subtotal - total_discount

            tax = amount_after_discount * tax_rate

            final_price = amount_after_discount + tax

            print("\n========== RECEIPT ==========")
            print("Subtotal:", subtotal)
            print("Discount:", discount)
            print("Coupon Discount:", coupon_discount)
            print("Total Discount:", total_discount)
            print("Tax:", tax)
            print("Final Amount:", final_price)

        elif choice == 3:
            print("Displaying Order History...")

        else:
            print("Invalid Option")

    # CASHIER MENU
    elif role == "Cashier":

        print("\n===== CASHIER MENU =====")
        print("1. Process Payment")
        print("2. Generate Receipt")
        print("3. Checkout Customer")

        choice = int(input("Choose an option: "))

        if choice == 1:
            print("Payment Processing Module...")

        elif choice == 2:
            print("Receipt Generation Module...")

        elif choice == 3:

            print("\n===== CUSTOMER CHECKOUT =====")

            subtotal = float(input("Enter Product Subtotal: "))
            location = input("Enter Location (Uganda/Kenya/Tanzania): ")
            coupon = input("Enter Coupon Code: ")

            # Discount based on subtotal
            if subtotal >= 500000:
                discount = subtotal * 0.20
            elif subtotal >= 200000:
                discount = subtotal * 0.10
            else:
                discount = subtotal * 0.05

            # Coupon validation
            if coupon == "SAVE10":
                coupon_discount = subtotal * 0.10

            elif coupon == "SAVE20":
                coupon_discount = subtotal * 0.20

            else:
                coupon_discount = 0
                print("Invalid Coupon Code")

            # Tax based on location
            if location.lower() == "uganda":
                tax_rate = 0.18

            elif location.lower() == "kenya":
                tax_rate = 0.16

            elif location.lower() == "tanzania":
                tax_rate = 0.18

            else:
                tax_rate = 0.10
                print("Unknown Location - Default Tax Applied")

            total_discount = discount + coupon_discount

            amount_after_discount = subtotal - total_discount

            tax = amount_after_discount * tax_rate

            final_price = amount_after_discount + tax

            print("\n========== RECEIPT ==========")
            print("Subtotal:", subtotal)
            print("Discount:", discount)
            print("Coupon Discount:", coupon_discount)
            print("Total Discount:", total_discount)
            print("Tax:", tax)
            print("Final Amount:", final_price)

        else:
            print("Invalid Option")