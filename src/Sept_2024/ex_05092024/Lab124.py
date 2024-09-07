# Inheritance

class Father:
    key = "2BHK"
    def car(self):
        print("Father Car!!", "ALTO",self.key)


class Son(Father):
    key2 = "3BHK"

    def home(self):
        print("3BHK")

    def truck(self):
        print("Truck")


father_obj = Father()
father_obj.car()
print(father_obj.key)
# print(father_obj.key2) cannot access key2 from Father Class
# father_obj.truck() cannot access Son class attribute and behaviour --> Error
print("------------------------")

son_obj = Son()
son_obj.car()
print(son_obj.key2)
son_obj.truck() # Son can access its own behaviour

