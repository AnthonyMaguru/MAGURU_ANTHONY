# Assignment 3: Real World Application of Loop Control Statements

print("===== WORLD CUP 2026 PREDICTION =====")

while True:
    country = input("\nEnter a country (or type EXIT to quit): ").strip()

    if country.upper() == "EXIT":
        print("Exiting prediction system...")
        break

    if country == "":
        print("Country name cannot be empty!")
        continue

    if country.upper() == "UGANDA":
        # Future special analysis for Uganda
        pass

    # Prediction logic
    favorites = ["BRAZIL", "ARGENTINA", "FRANCE", "ENGLAND", "SPAIN"]

    if country.upper() in favorites:
        print(f"{country} has a HIGH chance of winning World Cup 2026!")
    else:
        print(f"{country} has a LOW chance of winning World Cup 2026.")

print("Program ended.")