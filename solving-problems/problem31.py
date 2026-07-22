# ==========================================================
# Q1. Calculate Tax Rate Based on Salary
# ==========================================================

salary = float(input("Q1 - Enter your salary: "))

if salary < 30000:
    tax_rate = 5
elif salary <= 70000:
    tax_rate = 15
else:
    tax_rate = 25

tax_amount = salary * tax_rate / 100

print(f"Tax rate: {tax_rate}%")
print(f"Tax amount: {tax_amount:.2f}")


# ==========================================================
# Q2. Print All Even Numbers Between Two Integers
# ==========================================================

def print_even_numbers(a, b):
    start = min(a, b)
    end = max(a, b)

    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number, end=" ")

    print()


first_number = int(input("\nQ2 - Enter first number: "))
second_number = int(input("Enter second number: "))

print("Even numbers:")
print_even_numbers(first_number, second_number)


# ==========================================================
# Q3. Print the Digits of a Number
# ==========================================================

def print_digits(number):
    number = abs(number)

    if number == 0:
        print(0)
        return

    digits = []

    while number > 0:
        digit = number % 10
        digits.append(digit)
        number = number // 10

    digits.reverse()

    for digit in digits:
        print(digit, end=" ")

    print()


number = int(input("\nQ3 - Enter a number: "))

print("Digits are:")
print_digits(number)


# ==========================================================
# Q4. Count the Number of Digits
# ==========================================================

def count_digits(number):
    number = abs(number)

    if number == 0:
        return 1

    count = 0

    while number > 0:
        count += 1
        number = number // 10

    return count


number = int(input("\nQ4 - Enter a number: "))

print(f"Number of digits: {count_digits(number)}")


# ==========================================================
# Q5. Find the Sum of Digits
# ==========================================================

def sum_of_digits(number):
    number = abs(number)
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10

    return total


number = int(input("\nQ5 - Enter a number: "))

print(f"Sum of digits: {sum_of_digits(number)}")


# ==========================================================
# Q6. Numbers Divisible by Both 3 and 5
# ==========================================================

print("\nQ6 - Numbers from 1 to 100 divisible by both 3 and 5:")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(number, end=" ")

print()


# ==========================================================
# Q7. Check Positive or Negative Until User Enters Quit
# ==========================================================

print("\nQ7 - Enter numbers to check positive or negative.")

while True:
    user_input = input("Enter a number or type Quit: ")

    if user_input.lower() == "quit":
        print("Q7 program ended.")
        break

    try:
        number = float(user_input)

        if number > 0:
            print("Positive number")
        elif number < 0:
            print("Negative number")
        else:
            print("The number is zero")

    except ValueError:
        print("Please enter a valid number or type Quit.")


# ==========================================================
# Q8. Simple Calculator
# ==========================================================

def calculator(a, b, operation):
    if operation == "+":
        return a + b

    elif operation == "-":
        return a - b

    elif operation == "*":
        return a * b

    elif operation == "/":
        if b == 0:
            return "Error: Cannot divide by zero."

        return a / b

    else:
        return "Invalid operation."


first_number = float(input("\nQ8 - Enter first number: "))
second_number = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

result = calculator(first_number, second_number, operation)

print(f"Result: {result}")


# ==========================================================
# Q9. Check Whether a Number Is Prime
# ==========================================================

def is_prime(n):
    if n < 2:
        return False

    for number in range(2, n):
        if n % number == 0:
            return False

    return True


number = int(input("\nQ9 - Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


# ==========================================================
# Q10. Number Guessing Game
# ==========================================================

secret_number = 7

print("\nQ10 - Guess the secret number.")

while True:
    guess = int(input("Enter your guess: "))

    if guess > secret_number:
        print("Too high")

    elif guess < secret_number:
        print("Too low")

    else:
        print("Correct!")
        break
