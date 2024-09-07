# Hierarchical Inheritance

class Father:
    def BHK1(self):
        print("1BHK")


class Dhir(Father):
    def BHK2(self):
        print("2BHK")


class Chandni(Father):
    def BHK3(self):
        print("3BHK")


class Srush(Father):
    def no_house(self):
        print("NO house")

dhir1 = Dhir()
dhir1.BHK1()
dhir1.BHK2()

print("-----------------------")

chandni1 = Chandni()
chandni1.BHK1()
chandni1.BHK3()
# chandni1.BHK2()? This belong to dhir
