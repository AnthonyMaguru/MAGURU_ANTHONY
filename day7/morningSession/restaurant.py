#exe 9.1
"""class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


# Create an instance
restaurant = Restaurant("Fresh Hot KK", "Ugandan")

# Print attributes
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Call methods
restaurant.describe_restaurant()
restaurant.open_restaurant()"""

#exer 9.2
"""class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print()


# Create three instances
restaurant1 = Restaurant("Fresh Hot KK", "Ugandan")
restaurant2 = Restaurant("Fredoz Wandegeya", "Italian")
restaurant3 = Restaurant("Eko's Restaurant", "African")

# Call method for each restaurant
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()"""

#exer 9.3
class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print("User Information")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.\n")


# Create users
user1 = User("Anthony", "Maguru", 22, "anthony@gmail.com")
user2 = User("Suzanna", "Shomu", 20, "suzanna@gmail.com")
user3 = User("Nicholas", "Okello", 25, "nicholas@gmail.com")

# Call methods
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()