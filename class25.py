is_raining = False
is_cold = False
print('Good Morning!')
if is_raining and is_cold:
    print('Bring umbrella and jacket!')
elif is_raining and not(is_cold):
    print("Bring umbrella!")
elif not(is_raining) and is_cold:
    print("Bring jacket!")
else:
    print('Shirt is fine!')


amount = 10
if amount <= 50:
    print("Purchase approved")
else:
    print("Please enter your PIN")