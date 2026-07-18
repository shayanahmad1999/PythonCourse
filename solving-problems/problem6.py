print('Find the largest of three numbers')

def  find_largest(a,b,c):
    largest = a
    if b > largest:
        return f"{b} is largest than {a} and {c}"
    if c > largest:
        return f"{c} is largest than {a} and {b}"
    
    return f"{a} is largest than {b} and {c}"

num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))
num3 = int(input('Enter third number'))

result = find_largest(num1,num2,num3)
print(result)
