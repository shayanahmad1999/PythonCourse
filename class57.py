square = lambda x: x*x
print(square(4)) 

multiply = lambda x, y: x * y
print(multiply(5,3))

double_mul = lambda x,y: 2*x*y
print(double_mul(6,6))

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x%2 == 0, numbers))
print(evens)

odds = list(filter(lambda x: x%2 != 0, numbers))
print(odds)

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)


name_and_alias = lambda name,alias:name.strip().title() + ":" + alias.strip().title()
print(name_and_alias(' john  ClEEse  ','HECKLER'))

monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']
monty_python.sort(key = lambda name:name.split(' ')[-1])
print(monty_python)

pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
pairs.sort(key=lambda item: item[1])
print(pairs)
