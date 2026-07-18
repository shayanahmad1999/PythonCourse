print('Check whether a number is a palindrome')

def reverse_number(number):
    reverse_number = 0
    temporary = number
    while temporary > 0:
        digit = temporary % 10
        reverse_number = reverse_number * 10 + digit
        temporary //= 10

    return reverse_number

def is_palindrome(number):
    return number == reverse_number(number)

number = int(input("Enter a positive number: "))

if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
