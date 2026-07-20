print('Print prime numbers in a range')

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def print_primes(start, end):
    for number in range(start, end + 1):
        if is_prime(number):
            print(number, end=" ")

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers:")
print_primes(start, end)
