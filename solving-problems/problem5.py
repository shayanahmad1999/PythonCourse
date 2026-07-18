print('Find the larger of two numbers')

def find_larger(a, b):
    if a > b:
        return f"{a} is greater than {b}"
    elif b > a:
        return f"{b} is greater than {a}"
    else:
        return "Both are equal"
    
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
result = find_larger(num1, num2)
print(f"Result: {result}")
