print('Student subject registration system')

student_name = input("Enter student name: ")
number_of_subjects = int(input("How many subjects? "))

subject_list = []

for i in range(number_of_subjects):
    subject = input(f"Enter subject {i + 1}: ").strip().title()
    subject_list.append(subject)

unique_subjects = set(subject_list)
subject_tuple = tuple(unique_subjects)

student = {
    "name": student_name.title(),
    "subjects": subject_tuple,
    "subject_count": len(subject_tuple)
}

print("\n===== Student Information =====")
print("Name:", student["name"])
print("Subjects:", student["subjects"])
print("Total unique subjects:", student["subject_count"])
