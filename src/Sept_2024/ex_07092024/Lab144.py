# Static Methods
# A static method is a method that belongs to a
# class rather than an instance of the class.
class O:
    @staticmethod
    def sum(a, b):
        return a + b


class MathOperations(O):

    def div(self, a, b):
        return a / b

    def mul(self, a, b):
        return a * b

    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

class Maximum_value():
    @staticmethod
    def maxvalue(a,b):
        max1 = max(a,b)
        print("The maximum value between a and b is :", max1)


# Non Static in Nature - Object creation is mandatory
object_ref = MathOperations()
output = object_ref.div(10, 5)
output2 = object_ref.mul(10, 5)
print(output)
print(output2)

# Static methods can be called direclty without the Object.
print(MathOperations.sum(4, 5))
print(f"This is multiplication :", MathOperations.mul(4,4,4))
print(MathOperations.sub(4, 5))  # MathOperations.div() missing 1 required positional argument: 'b
print(O.sum(4, 5))  # MathOperations.div() missing 1 required positional argument: 'b

Maximum_value.maxvalue(10, 20)
print("********************")
Maximum_value.maxvalue(5, 3)
