print('Remove duplicate values while keeping order')

numbers = [10, 20, 10, 30, 20, 40, 10]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("Original list:", numbers)
print("Without duplicates:", unique_numbers)