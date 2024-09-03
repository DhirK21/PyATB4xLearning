age = 65
# 123 = 34 -> Not Possible - A-Z, a-z
a = 10
# They start with a letter (A-Z or a-z)
# an underscore (_) follwed by zero or more letters,
# underscore, and digits (0-9).
# Python is case sensitive.
# so myVariable and myvariable are two different identifiers

a = 10
_ = 45
_ = _+1
print(_)

abc123 = 78
#123abc = 90 not valid
_pramod = "amit"
_abc = 23
#$123 = 67 Not allowed
#&123 = 23 Not allowed

pi = 3.14 #Float
name = "Pramod" #String
isMale= True
print(type(name))
print(type(isMale))
print(type(pi))

complex_number = 2 + 3j
print(complex_number.real)
print(complex_number.imag)