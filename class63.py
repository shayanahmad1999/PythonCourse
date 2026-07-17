# 🏆 Raffle Prize Picker — Challenge Steps
#
# 1. Ask how many people are entering the raffle (at least 3 names).
# 2. Use a loop to collect their names into a list.
# 3. Ask for exactly 3 prize names (in order) and store them in a list.
# 4. Randomly pick 3 different winners from the participant list.
# 5. Print out who wins which prize and make sure the final one
#    is clearly marked as the Grand Prize. 🏆
#
# Hint: Use loops, lists, and a tool that picks random items without repeats.

import random

participants = []
prizes = []

# Ask for the number of participants
while True:
    number_of_people = int(input("How many people are entering the raffle? "))

    if number_of_people >= 3:
        break
    else:
        print("At least 3 people are required.")

# Collect participant names
for i in range(number_of_people):
    name = input(f"Enter participant {i + 1} name: ").strip()
    participants.append(name)

# Collect exactly 3 prizes
for i in range(3):
    prize = input(f"Enter prize {i + 1}: ").strip()
    prizes.append(prize)

# Pick 3 different winners
winners = random.sample(participants, 3)

print("\n🎉 ===== Raffle Results ===== 🎉")

for i in range(3):
    if i == 2:
        print(f"🏆 GRAND PRIZE: {winners[i]} wins {prizes[i]}!")
    else:
        print(f"🎁 {winners[i]} wins {prizes[i]}!")
