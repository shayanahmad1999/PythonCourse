def nameNotaion(name, age, color):
    print(f'Hello {name.capitalize()}, you will be {age+1} next birthday!')
    print(f'We hear you like the color {color.lower()}!')

# nameNotaion(27, "Alice", 'red') # its throw error because of un-order

nameNotaion(age = 27, name = 'Alice', color = 'blue') # its not throw error because of name notaion in the function 