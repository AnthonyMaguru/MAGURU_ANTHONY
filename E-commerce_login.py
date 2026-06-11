print("===== E-COMMERCE LOGIN SYSTEM =====")

username = input("Username: ")
password = input("Password: ")

logged_in = False

if username == "admin":
    if password == "admin123":
        print("Welcome Admin")
        logged_in = True
    else:
        print("Incorrect Password")

elif username == "customer":
    if password == "cust123":
        print("Welcome Customer")
        logged_in = True
    else:
        print("Incorrect Password")

elif username == "cashier":
    if password == "cash123":
        print("Welcome Cashier")
        logged_in = True
    else:
        print("Incorrect Password")

else:
    print("User not found")

# Proceed only if login succeeds
if logged_in:

    print("\n===== CHECKOUT SYSTEM =====")

    subtotal = float(input("Enter subtotal: "))
    coupon = input("Enter coupon code: ")

    tax_countries = {
        "1": ("Uganda", 0.18),
        "2": ("Kenya", 0.16),
        "3": ("Tanzania", 0.18),
        "4": ("Other", 0.10),
    }

    print("\nSelect country for tax:")
    for number, (country, rate) in tax_countries.items():
        print(f"{number}. {country}")

    country_choice = input("Enter the number for the country: ")
    location, tax_rate = tax_countries.get(country_choice, ("Other", 0.10))

    # Discount levels
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

    total_discount = discount + coupon_discount

    amount_after_discount = subtotal - total_discount

    tax = amount_after_discount * tax_rate

    final_price = amount_after_discount + tax

    print("\n===== INVOICE =====")
    print("Subtotal:", subtotal)
    print("Discount:", total_discount)
    print("Tax:", tax)
    print("Final Amount:", final_price)