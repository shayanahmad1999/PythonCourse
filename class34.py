# ==========================================
# PYTHON sort() vs sorted() - Complete Examples
# ==========================================

# -------------------------------
# 1. LIST
# -------------------------------
numbers = [5, 2, 8, 1, 9]

# sort() -> modifies original list
numbers.sort()
print("List using sort():", numbers)

# sorted() -> returns a new sorted list
numbers = [5, 2, 8, 1, 9]
new_numbers = sorted(numbers)
print("List using sorted():", new_numbers)
print("Original:", numbers)


# -------------------------------
# 2. LIST (Descending)
# -------------------------------
numbers = [5, 2, 8, 1, 9]

numbers.sort(reverse=True)
print("sort(reverse=True):", numbers)

numbers = [5, 2, 8, 1, 9]
print("sorted(reverse=True):", sorted(numbers, reverse=True))


# -------------------------------
# 3. LIST (Sort by Length)
# -------------------------------
words = ["banana", "kiwi", "apple", "grape"]

words.sort(key=len)
print("sort(key=len):", words)

words = ["banana", "kiwi", "apple", "grape"]
print("sorted(key=len):", sorted(words, key=len))


# -------------------------------
# 4. TUPLE
# -------------------------------
numbers = (5, 2, 8, 1, 9)

print("Tuple:", numbers)

# numbers.sort()      # ERROR

print("sorted(tuple):", sorted(numbers))


# -------------------------------
# 5. SET
# -------------------------------
numbers = {5, 2, 8, 1, 9}

print("Set:", numbers)

# numbers.sort()      # ERROR

print("sorted(set):", sorted(numbers))


# -------------------------------
# 6. STRING
# -------------------------------
text = "python"

print("String:", text)

# text.sort()         # ERROR

print("sorted(string):", sorted(text))

# Join back into a string
print("''.join(sorted(text)):", "".join(sorted(text)))


# -------------------------------
# 7. DICTIONARY (Keys)
# -------------------------------
student = {
    "name": "Ali",
    "age": 20,
    "city": "Peshawar"
}

print("Dictionary:", student)

# student.sort()      # ERROR

print("sorted(dictionary):", sorted(student))
print("sorted(dictionary.keys()):", sorted(student.keys()))


# -------------------------------
# 8. DICTIONARY (Values)
# -------------------------------
marks = {
    "Ali": 85,
    "Ahmed": 72,
    "Sara": 91,
    "John": 65
}

print("sorted(values):", sorted(marks.values()))


# -------------------------------
# 9. DICTIONARY (Items)
# -------------------------------
print("sorted(items):")
print(sorted(marks.items()))


# -------------------------------
# 10. Sort Dictionary by VALUE
# -------------------------------
print("Sort dictionary by values:")

print(
    sorted(
        marks.items(),
        key=lambda item: item[1]
    )
)


# -------------------------------
# 11. Sort Dictionary by KEY
# -------------------------------
print("Sort dictionary by keys:")

print(
    sorted(
        marks.items(),
        key=lambda item: item[0]
    )
)


# -------------------------------
# 12. Sort Dictionary by VALUE Descending
# -------------------------------
print(
    sorted(
        marks.items(),
        key=lambda item: item[1],
        reverse=True
    )
)


# -------------------------------
# 13. List of Tuples
# -------------------------------
students = [
    ("Ali", 85),
    ("Ahmed", 72),
    ("Sara", 91),
    ("John", 65)
]

print(sorted(students))

print(
    sorted(
        students,
        key=lambda student: student[1]
    )
)


# -------------------------------
# 14. List of Dictionaries
# -------------------------------
employees = [
    {"name": "Ali", "salary": 30000},
    {"name": "Ahmed", "salary": 25000},
    {"name": "Sara", "salary": 40000}
]

employees.sort(key=lambda emp: emp["salary"])

print(employees)


# -------------------------------
# 15. Ignore Upper/Lower Case
# -------------------------------
names = ["ali", "Ahmed", "john", "Sara"]

print(sorted(names))
print(sorted(names, key=str.lower))


# -------------------------------
# 16. Numbers as Strings
# -------------------------------
numbers = ["100", "20", "5", "80"]

print(sorted(numbers))
print(sorted(numbers, key=int))


# -------------------------------
# 17. Return Value
# -------------------------------
numbers = [3, 1, 2]

result = numbers.sort()

print(result)      # None
print(numbers)


# ==========================================
# END
# ==========================================