print('Find the second-largest number')

numbers = [10, 50, 30, 50, 40]

unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)

if len(unique_numbers) >= 2:
    print("Second-largest number:", unique_numbers[1])
else:
    print("A second-largest number does not exist.")