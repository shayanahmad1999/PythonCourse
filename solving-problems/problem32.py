# ==========================================================
# Q1. Check Whether a String Is a Palindrome
# ==========================================================

text = input("Q1 - Enter a string: ").lower()

reversed_text = ""

for character in text:
    reversed_text = character + reversed_text

if text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# ==========================================================
# Q2. Find the Average of Numbers in a List
# ==========================================================

numbers = input("\nQ2 - Enter numbers separated by spaces: ").split()

number_list = []

for number in numbers:
    number_list.append(int(number))

total = sum(number_list)
average = total / len(number_list)

print("List:", number_list)
print("Average:", average)


# ==========================================================
# Q3. Merge and Sort Two Lists
# ==========================================================

first_input = input(
    "\nQ3 - Enter numbers for the first list separated by spaces: "
).split()

second_input = input(
    "Enter numbers for the second list separated by spaces: "
).split()

list1 = []
list2 = []

for number in first_input:
    list1.append(int(number))

for number in second_input:
    list2.append(int(number))

merged_list = list1 + list2
merged_list.sort()

print("First list:", list1)
print("Second list:", list2)
print("Merged and sorted list:", merged_list)


# ==========================================================
# Q4. Create Even and Odd Tuples
# ==========================================================

tuple_input = input(
    "\nQ4 - Enter tuple numbers separated by spaces: "
).split()

numbers_list = []

for number in tuple_input:
    numbers_list.append(int(number))

numbers_tuple = tuple(numbers_list)

even_numbers = []
odd_numbers = []

for number in numbers_tuple:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

even_tuple = tuple(even_numbers)
odd_tuple = tuple(odd_numbers)

print("Original tuple:", numbers_tuple)
print("Even tuple:", even_tuple)
print("Odd tuple:", odd_tuple)


# ==========================================================
# Q5. Student Marks Dictionary Menu
# ==========================================================

students = {}

while True:
    print("\n===== Student Menu =====")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students")
    print("E - Exit")

    choice = input("Enter your choice: ").upper()

    if choice == "A":
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))

        if name in students:
            print("Student already exists.")
        else:
            students[name] = marks
            print("Student added successfully.")

    elif choice == "B":
        name = input("Enter student name: ")

        if name in students:
            new_marks = int(input("Enter new marks: "))
            students[name] = new_marks
            print("Marks updated successfully.")
        else:
            print("Student not found.")

    elif choice == "C":
        name = input("Enter student name: ")

        if name in students:
            print(f"{name}'s marks: {students[name]}")
        else:
            print("Student not found.")

    elif choice == "D":
        if students:
            print("\nStudents and marks:")

            for name, marks in students.items():
                print(f"{name}: {marks}")
        else:
            print("No students found.")

    elif choice == "E":
        print("Student program ended.")
        break

    else:
        print("Invalid choice.")


# ==========================================================
# Q6. Create a Dictionary of Words and Their Lengths
# ==========================================================

words = ["apple", "banana", "kiwi", "cherry", "mango"]

word_lengths = {}

for word in words:
    word_lengths[word] = len(word)

print("\nQ6 - Word lengths:")
print(word_lengths)


# ==========================================================
# Q7. Count Spaces in a String
# ==========================================================

sentence = input("\nQ7 - Enter a sentence: ")

space_count = 0

for character in sentence:
    if character == " ":
        space_count += 1

print("Number of spaces:", space_count)


# ==========================================================
# Q8. Check Whether Two Lists Have Common Elements
# ==========================================================

first_input = input(
    "\nQ8 - Enter numbers for the first list separated by spaces: "
).split()

second_input = input(
    "Enter numbers for the second list separated by spaces: "
).split()

list1 = []
list2 = []

for number in first_input:
    list1.append(int(number))

for number in second_input:
    list2.append(int(number))

set1 = set(list1)
set2 = set(list2)

common_elements = set1.intersection(set2)

if len(common_elements) == 0:
    print("The lists share no common elements.")
else:
    print("The lists have common elements.")
    print("Common elements:", common_elements)


# ==========================================================
# Q9. Print Duplicate Elements from a List
# ==========================================================

numbers = input(
    "\nQ9 - Enter list numbers separated by spaces: "
).split()

number_list = []

for number in numbers:
    number_list.append(int(number))

seen = set()
duplicates = set()

for number in number_list:
    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)

if duplicates:
    print("Duplicate elements:", duplicates)
else:
    print("There are no duplicate elements.")


# ==========================================================
# Q10. Print Unique Characters and Their Count
# ==========================================================

text = input("\nQ10 - Enter a string: ")

unique_characters = set(text)

print("Unique characters:", unique_characters)
print("Number of unique characters:", len(unique_characters))
