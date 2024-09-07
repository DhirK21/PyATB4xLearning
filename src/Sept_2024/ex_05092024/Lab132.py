# Hybrid Inheritance

# multiple types of inheritance,
# such as single,
# multiple, and
# multilevel inheritance.

class A: # Father
    def methodA(self):
        return "Method A"

class B(A): # Dhir
    def methodB(self):
        return "Method B"

class C(A): # Srush
    def methodC(self):
        return "Method C"


class D(B, C): #Chandni  # Multiple, Multilevel - MRO(Method Resolution Order - First
    def methodD(self):
        return "Method D"

d = D()
print(d.methodA())
print(d.methodB())
print(d.methodD())
print(d.methodC())