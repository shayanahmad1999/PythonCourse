print('Reverse a number')

def reverse_number(number):
    reverse_number = 0

    while number > 0:
        digit = number % 10
        reverse_number = reverse_number * 10 + digit
        number //= 10
    return reverse_number

number = int(input("Enter a positive number: "))
result = reverse_number(number)

print(f"Reversed number: {result}")
