print('Find the sum of digits')

def sum_of_digits(number):
    number = abs(number)

    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

number = int(input("Enter a number: "))
result = sum_of_digits(number)

print(f"Sum of digits: {result}")
    