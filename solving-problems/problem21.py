print('Calculate marks and grade')

def calculate_percentage(obtained_marks, total_marks):
    return obtained_marks/total_marks * 100

def find_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"

obtained = float(input('Enter obtained marks: '))    
total = float(input('Enter total marks: '))

if total <= 0:
    print("Total marks must be greater than zero.")
else:
    percentage = calculate_percentage(obtained, total)
    grade = find_grade(percentage)
    
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

