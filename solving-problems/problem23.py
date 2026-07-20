print('Find the largest number in a list')

def find_list_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
    return largest

numbers = []

for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

result = find_list_largest(numbers)

print(f"Number: {numbers}")
print(f"Larges number: {result}")
