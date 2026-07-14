with open('files/writing.txt', 'w') as f:
    f.write("Hello, World!")


with open('files/writing.txt', 'w') as f:
    f.write("The Dark Knight\n")
    f.write("Inception\n")
    f.write("Interstellar\n")

movies = [
    "The Dark Knight\n",
    "Inception\n",
    "Interstellar\n"
]

with open('files/writing.txt', 'w') as f:
    f.writelines(movies)

name = input("Enter your name: ")

with open('files/names.txt', 'w') as f:
    f.write(name)


with open('files/students.txt', 'w') as f:
    for i in range(3):
        name = input("Enter student name: ")
        f.write(name + "\n")
