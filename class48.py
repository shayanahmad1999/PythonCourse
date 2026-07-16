class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(self.fname, self.lname)


class Student(Person):
    pass


class Employee(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

    def welcome(self):
        print(
            "Welcome",
            self.fname,
            self.lname,
            "to the France Team in the year",
            self.year
        )


person = Person("John", "Doe")
person.print_name()

student = Student("Mike", "Olsen")
student.print_name()

employee = Employee("Kylian", "Mbappe", 2017)
employee.print_name()
employee.welcome()




class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating.")


class Dog(Animal):
    def bark(self):
        print(self.name, "is barking.")


dog = Dog("Buddy")
dog.eat()
dog.bark()
