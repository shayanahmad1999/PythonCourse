class Pizza:
    def __init__(self, size, crust, toppings=None):
        self.size = size
        self.crust = crust
        self.toppings = toppings if toppings is not None else []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)
            print(f"{topping.title()} was removed.")
        else:
            print(f"{topping.title()} isn't on your pizza.")

    def describe_pizza(self):
        print("\n🍕 ===== Your Pizza ===== 🍕")
        print(f"Size: {self.size.title()}")
        print(f"Crust: {self.crust.title()}")

        if self.toppings:
            print("Toppings:")
            for topping in self.toppings:
                print(f" - {topping.title()}")
        else:
            print("No toppings added!")


# Get pizza information from the user
size = input("Enter pizza size: ").strip()
crust = input("Enter crust type: ").strip()

my_pizza = Pizza(size, crust)

# Ask how many toppings the user wants
while True:
    try:
        topping_count = int(input("How many toppings do you want? "))

        if topping_count >= 0:
            break

        print("Please enter 0 or a positive number.")

    except ValueError:
        print("Please enter a valid number.")


# Add toppings
for number in range(topping_count):
    topping = input(f"Enter topping {number + 1}: ").strip()

    if topping:
        my_pizza.add_topping(topping)


# Ask whether the user wants to remove a topping
remove_choice = input(
    "Do you want to remove a topping? (yes/no): "
).strip().lower()

if remove_choice == "yes":
    topping_to_remove = input(
        "Enter the topping you want to remove: "
    ).strip()

    my_pizza.remove_topping(topping_to_remove)


# Display the final pizza
my_pizza.describe_pizza()