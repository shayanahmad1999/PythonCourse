class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printName(self):
        print(self.fname, self.lname)

x = Person('John', 'Doe')
x.printName()

class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printName()


class Animal(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Animal('Dogesh', 'babu')
x.printName()


class Employee(Animal):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

    def welcome(self):
        print("Welcome ",self.fname, self.lname, "to the France Team in the year of ", self.year)

x = Employee('Kylian', 'Mbappe', 2017)
x.welcome()

