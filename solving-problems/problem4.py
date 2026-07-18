print('Check positive, negative, or zero')

def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
    
number = int(input('Enter a number: '))
result = check_number(number)
print(f'The number is {result}')
