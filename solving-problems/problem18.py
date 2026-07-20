print('Find the greatest common divisor')

def find_gcd(a, b):
    a = abs(a)
    b = abs(b)

    while b != 0:
        reminder = a % b
        a = b
        b = reminder
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = find_gcd(num1, num2)
print(f"GCD of {num1} and {num2} is: {result}")
