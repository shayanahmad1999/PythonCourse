print('Find the square of a number')

def square(number):
    return number * number

number = int(input('Enter a number: '))
result = square(number)
print(f"Square of {number} is: {result}")
