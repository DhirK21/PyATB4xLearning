class Dog: # class Name will always start from the Capital letter
    # Attributes
    name = None
    breed = None
    color = None

    # Behaviour
    def sleep(self):
        print("Dog is Sleeping")

    def walk(self):
        print("Dog is walking")

    def bark(self):
        print("Dog is barking")

    def eat(self, food):
        print(food)


# Object defined from the class

dog1 = Dog()
dog1.name = "Tanu"
print(dog1.name)
dog1.sleep()

print("----------------------")

dog2 = Dog()
dog2.name = "Minu"
dog2.color = "black"
dog2.eat("Dog Biscuits")
print(dog2.color)
print(dog2.name)

print("----------------------")

dog1.walk()

print("----------------------")

dog3 = dog2 # To create duplicate values from the object
print(dog3.name)

