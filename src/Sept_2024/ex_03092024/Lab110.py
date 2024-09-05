# Take input and create a class in python

class Person:

    # Define Constructor
    def __init__(self):
        self.name = input("Enter the name :")
        self.age = input("Enter the age :")
        self.phone = int(input("Enter the phone no :"))
        self.occupation = input("Enter the type of occupation :")

    def name_of_the_function_to_display(self):
        print(f" Name is : {self.name}\n", f" Age is : {self.age}\n", f" The phone number is : {self.phone}\n", f" The occupation is : {self.occupation}")

# Creating an object from the class

person1 = Person()

# Call the display function
person1.name_of_the_function_to_display()