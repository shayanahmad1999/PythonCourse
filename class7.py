# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

name = input('Enter Your Name:')
# formatted_name = name.capitalize()
formatted_name = name.title()

distance_in_km = float(input('Enter distance in kilometers: '))
distance_in_miles = distance_in_km / 1.609

print(f"Hello, {formatted_name}! {distance_in_km:.2f} km is equal to {distance_in_miles:.2f} miles.")
