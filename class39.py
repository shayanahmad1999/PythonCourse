# 🐾 Dog Bus Tracker — Challenge Steps
#
# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time
#
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.
#
# 3. Add one new pet if there’s room on the bus.  
#    - Use MAX_SEATS to limit capacity.  
#    - Dynamically assign the next seat number.  
#    - Print the updated roster showing all pets after pickup.  
#
# 4. Ask which pet leaves early.  
#    - Remove that pet from the bus.  
#    - Print a message saying they’ve headed home.  
#
# 5. Print a final roster listing the remaining pets and their dropoff times.

MAX_SEATS = 8

bus = {
  1: {"name": "Milo", "breed": "Labrador", "pickup": "8:00 AM", "dropoff": "4:00 PM"},
  2: {"name": "Otis", "breed": "French Bulldog", "pickup": "8:15 AM", "dropoff": "4:15 PM"},
  3: {"name": "Willow", "breed": "Border Collie", "pickup": "8:30 AM", "dropoff": "4:30 PM"},
}

print("===== Starting Roster =====")

for seat, info in bus.items():
    print(f"Seat {seat}: {info['name']} (pickup {info['pickup']})")

if len(bus) < MAX_SEATS:
    new_name = input("\nEnter the new pet's name: ")
    new_breed = input("Enter the pet's breed: ")
    new_pickup = input("Enter the pickup time: ")
    new_dropoff = input("Enter the dropoff time: ")

    next_seat = max(bus.keys()) + 1

    bus[next_seat] = {
        "name": new_name,
        "breed": new_breed,
        "pickup": new_pickup,
        "dropoff": new_dropoff
    }

    print(f"\n{new_name} has been added to seat {next_seat}.")

else:
    print("\nThe bus is full.")

print("\n===== Updated Roster =====")

for seat, info in bus.items():
    print(
        f"Seat {seat}: {info['name']} - Pickup: {info['pickup']}"
    )

leaving_pet = input("\nWhich pet is leaving early? ")

pet_found = False

for seat, pet in list(bus.items()):
    if pet["name"].lower() == leaving_pet.lower():
        del bus[seat]
        print(f"{pet['name']} has headed home.")
        pet_found = True
        break

if not pet_found:
    print("Pet not found on the bus.")

print("\n===== Final Roster =====")

for seat, info in bus.items():
    print(
        f"Seat {seat}: {info['name']} - Dropoff: {info['dropoff']}"
    )