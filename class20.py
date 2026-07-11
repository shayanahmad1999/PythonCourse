def greeting():
    print("Hello, welcome to the program!")

greeting()

def add_number(a,b):
    print(a + b)

add_number(5, 10)

def userName(name):
    print("Hello, " + name + "!")

userName("Alice")

def age(years):
    print(f"You are {years} years old.")

age(25)


def info(name, age, country = "pakistan"):
    print(f"Hello {name.title()}, your are {age}, and you from {country.capitalize()}")

name = input('Enter Your name: ')
age = input('Enter Your age: ')

info(name, age)
