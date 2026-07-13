#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
#Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
#ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

# Create stores
freelancers = {
    "name": "Freelancing Shop",
    "brian": 70,
    "black knight": 20,
    "biggus dickus": 100,
    "grim reaper": 500,
    "minstrel": -15
}

antiques = {
    "name": "Antique Shop",
    "french castle": 400,
    "wooden grail": 3,
    "scythe": 150,
    "catapult": 75,
    "german joke": 5
}

pet_shop = {
    "name": "Pet Shop",
    "blue parrot": 10,
    "white rabbit": 5,
    "newt": 2
}

# Create an empty shopping cart
cart = {}

# Visit each store
for shop in (freelancers, antiques, pet_shop):

    print(f"\nWelcome to {shop['name']}!")
    print("Available items:")

    # Show items without showing the shop name
    for item, price in shop.items():
        if item != "name":
            print(f"- {item.title()}: {price} Gp")

    buy_item = input(
        "What do you want to buy? Type 'exit' to leave: "
    ).strip().lower()

    # Leave the current shop without buying
    if buy_item == "exit":
        print("You left the shop without buying anything.")
        continue

    # Check whether the item exists
    if buy_item not in shop or buy_item == "name":
        print("That item does not exist. Moving to the next shop.")
        continue

    # Remove the item from the shop and add it to the cart
    item_price = shop.pop(buy_item)
    cart[buy_item] = item_price

    print(f"You took {buy_item.title()}.")

# Print final purchase summary
print("\n===== Shopping Cart =====")

if cart:
    buy_items = ", ".join(cart.keys())

    print(f"You purchased: {buy_items.title()}")
    print("Today it is all free.")
    print("Have a nice day of mayhem!")
else:
    print("You did not purchase anything.")