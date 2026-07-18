print('Count the digits in a number')

def count_digits(number):
    number = abs(number)

    if number == 0:
        return 1
    
    count = 0

    while number > 0:
        number //= 10
        count += 1
    return count

number = int(input('Enter a number: '))
result = count_digits(number)

print(f"Number of digits: {result}")
