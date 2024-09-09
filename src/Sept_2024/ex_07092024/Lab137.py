# Method Overriding - Same name in the parent and child
# child always override the parent functions
# super means call my parent function
class GrandFather:
    x = 12
    def home(self):
        print("Old Home")

class Father(GrandFather):
    a = 10
    def home(self):
        print("1BHK")
        print(self.a)
        print(super().x)

class Son(Father):
    b = 15
    def home(self):
        super().home() # Father Behaviour by super()
        print(super().a) # Father Attributes by super()
        print("No House")
        print(self.b)


        # self - me
        # super() - Parent, Super class, Father

dhir = Father()
dhir.home()
print("********************")
print(dhir.x)
print("********************")
dhir = Son()
dhir.home()