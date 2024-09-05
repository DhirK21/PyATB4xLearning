# Creating Calc Program:

class Calc():
    def __init__(self):
        print("DC")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def div(self, a, b):
        return a / b

    def mul(self, a, b):
        return a * b

# Creating the object from the class

calc1 = Calc()

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

output_of_sum = calc1.sum(a,b)
output_of_sub = calc1.sub(a,b)
output_of_div = calc1.div(a,b)
output_of_mul = calc1.mul(a,b)

print(f"The sum of a and b is: {output_of_sum} \n", f"The sub of a and b is: {output_of_sub}\n", f"The div of a and b is: {output_of_div} \n", f"The div of a and b is: {output_of_mul} \n")