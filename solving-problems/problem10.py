print('Calculate the power of a number')

def calculate_power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
answer = calculate_power(base, exponent)
print(f"{base} raised to {exponent} is: {answer}")
