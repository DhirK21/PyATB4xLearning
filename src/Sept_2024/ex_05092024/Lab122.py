a = 10
class Myclass:

    # public var (instance)
    public_var = "I am PUBLIC"
    __balance = 100
    balance = 100

    # Private variable
    __private_var = "I am private."
    __password = "1234"


    # Protected variable
    _protected_var = "I am protected."
    b = 10
    _c = 20
    __d = 45
    college = "ABC"
    pramod =  "TTA"
    __pramod_bank =  100000000000




object = Myclass()
print(object.public_var)
print(object._protected_var)
print(object.balance)
# print(object.__balance) # private variable
# print(object.__private_var) # private variable
# print(object.__password)