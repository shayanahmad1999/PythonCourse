print('Calculate the sum of a list')

def calculate_list_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total

numbers = []

count = int(input('How many numbers do you want to enter? '))

for i in range(count):
    number = float(input(f'Enter number {i + 1}: '))
    numbers.append(number)

result = calculate_list_sum(numbers)

print(f"Numbers: {numbers}")
print(f"Total: {result}")
