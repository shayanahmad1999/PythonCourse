print('Count even and odd numbers')

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for number in numbers:
        if number %2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return even_count, odd_count

numbers = []

count = int(input('How many numbers do you wan to enter? '))

for i in range(count):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

even, odd = count_even_odd(numbers)

print(f"Numbers: {numbers}")
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")
