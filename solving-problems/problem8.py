print('Find the sum from 1 to n')

def  calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

number = int(input('Enter a number: '))
result = calculate_sum(number)
print(f"Sum from 1 to {number} is: {result}")
    