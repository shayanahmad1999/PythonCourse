print('Project - Trading game simulation / pseudo code')
#create a bag with 10 marbles
#starting amount of money
# current money amount
#result of last round
#how many rounds
#last marble
# welcome user to game
# loop drawing marbles
    #how much was bet
    #draw marble
    # win or loss
    #calc win or loss/ result and new amount/purse
    #lose game if lose half of money
    #print results
# print final results


import random

print("Project - Trading Game Simulation")

# Create a bag containing 10 marbles
bag = (
    "green", "green", "green", "green", "green",
    "black",
    "red", "red", "red",
    "white"
)

# Game settings
start_purse = 1000
purse = start_purse
rounds = 3
marble = "none"

print("\n===== Welcome to the Marble Trading Game =====")
print(f"You start with {start_purse} gold pieces.")

print("\nMarble rules:")
print("Green: Win your bet")
print("Black: Win 10 times your bet")
print("Red: Lose your bet")
print("White: Lose 5 times your bet")

# Play the rounds
for current_round in range(1, rounds + 1):

    print(f"\n===== Round {current_round} =====")
    print(f"Current purse: {purse}")
    print(f"Last marble: {marble}")

    # Validate the bet
    while True:
        try:
            bet = int(input("How much do you want to bet? "))

            if bet <= 0:
                print("Your bet must be greater than 0.")

            elif bet > purse:
                print("You cannot bet more than your current purse.")

            else:
                break

        except ValueError:
            print("Please enter a valid whole number.")

    # Draw a random marble
    marble = random.choice(bag)

    # Calculate the result
    if marble == "green":
        result = bet

    elif marble == "black":
        result = 10 * bet

    elif marble == "white":
        result = -5 * bet

    else:  # Red marble
        result = -bet

    # Update the purse
    purse += result

    # Display the round result
    print(f"\nYou drew a {marble.upper()} marble.")

    if result > 0:
        print(f"You won {result} gold pieces!")
    else:
        print(f"You lost {abs(result)} gold pieces!")

    print(f"Your new purse is: {purse}")

    # End game after losing half the starting money
    if purse < start_purse * 0.5:
        print("\nGame over! You lost too much gold!")
        break

# Calculate final gain or loss
percentage = ((purse - start_purse) / start_purse) * 100

print("\n===== Final Results =====")
print(f"Starting purse: {start_purse}")
print(f"Ending purse: {purse}")

if purse > start_purse:
    print(f"Total profit: {purse - start_purse}")
    print(f"Percentage gained: {percentage:.2f}%")

elif purse < start_purse:
    print(f"Total loss: {start_purse - purse}")
    print(f"Percentage lost: {abs(percentage):.2f}%")

else:
    print("You finished with exactly the same amount!")
