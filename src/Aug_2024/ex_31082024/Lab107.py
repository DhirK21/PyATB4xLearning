class Person:
    # Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone = None
    address = None

    # Behaviour
    def talk(self): #NRNG # self -> this, self will be first argument in every behaviour
        print("I can talk")

    def sleep(self, name): # Arg with No return type
        print("I am a Method !!")
        print("Sleep", name)

    def sleep2(self, name): # Arg with return type
        print("I am a Method !!")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self): # No Arg with return type
        return "I am walking"

# Create an Object of the Class
# ObjectRef = ClassName() --> Object


Dhir_var1 = Person()
Dhir_var1.name = "Dhir"
print(Dhir_var1.name)

print("**********************")
# Different Object then previous --> Dhir_var1
Srush_var1 = Person()
Srush_var1.name = "Srushti"
print(Srush_var1.name)


