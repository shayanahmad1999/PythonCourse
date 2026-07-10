# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available


# 🕹️ Arcade Day Pass Tracker

# 1) Create variables
customer_name = "Alice"
passes = 10
tokens_per_pass = 2
price_per_pass = 20.00
tokens_required_per_game = 2

# 2) Calculate
total_tokens = passes * tokens_per_pass
total_cost = passes * price_per_pass
games_available = total_tokens // tokens_required_per_game

# 3) Print summary
print("===== ARCADE DAY PASS =====")
print(f"Customer Name: {customer_name}")
print(f"Passes Bought: {passes}")
print(f"Total Tokens: {total_tokens}")
# print(f"Total Cost: $" + str(total_cost))
print(f"Total Cost: ${total_cost:.2f}")
print(f"Games Available: {games_available}")