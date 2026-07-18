print('Create a multiplication table')

def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n * i}")

number = int(input('Enter a number: '))
multiplication_table(number)
