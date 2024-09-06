# Encapsulation -
# Hide the data members(class variables, instance variables)
# by using only the methods.

class Car:
    model = None
    name = None
    password = 123 # This variable should be private in nature

    # def __init__(self):
    #   print("DC")
    def __init__(self):
     self.password = "dhir"

    def change_password(self):
        print(self.password)


object_ref = Car()
print(object_ref.password)
object_ref.change_password() # used by outside the class --> obj reference
