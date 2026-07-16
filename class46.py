# Create a class
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
       print("Hello, my name is ", self.name) 
       print("My age is ", self.age) 

# Create an object
p1 = Person("John", 36)

# Call the greet method
p1.greet()



# Create the Dog class
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print("says Woof!: ", self.name)
        print("Age: ", self.age)
# Create an object
d1 = Dog("Buddy",3)
# Call the bark method
d1.bark()


