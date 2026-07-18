print('Calculate factorial')

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

number = int(input('Enter a non-negative number: '))
result = factorial(number)
print(f"Factorial of {number} is: {result}")
