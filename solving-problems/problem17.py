print('Generate a Fibonacci sequence')

def fibonacci(no_of_terms):
    first = 0
    second = 1

    for i in range(no_of_terms):
        print(first, end=" ")

        next_number = first + second
        first = second
        second = next_number

terms = int(input('How many terms do you want? '))
if terms <= 0:
    print('Please enter a postive number')
else:
    fibonacci(terms)
