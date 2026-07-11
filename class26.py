# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

opertaor = input('Enter Operator.And the Operator must be (+,-,*,/,%,//,f): ')
first_number = float(input('Enter any First number: '))
if opertaor.lower() == 'f':
    print(f'{first_number} Celsius is equivalent to: {(first_number*9/5) + 32} fahrenheit')
else:
    second_number = float(input('Enter any Second number: '))

    if opertaor == '+':
        print(f'Sum of two number is: {first_number+second_number}')
    elif opertaor == '-':
        print(f'Subtraction of two number is: {first_number-second_number}')
    elif opertaor == '*':
        print(f'Multiplication of two number is: {first_number*second_number}')
    elif opertaor == '/':
        print(f'Devision of two number is: {first_number/second_number}')
    elif opertaor == '%':
        print(f'Modulus of two number is: {first_number%second_number}')
    elif opertaor == '//':
        print(f'Devision floor of two number is: {first_number//second_number}')
    else:
        print('Invalid Operator')