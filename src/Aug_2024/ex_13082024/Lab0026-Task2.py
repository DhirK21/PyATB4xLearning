num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))

print(type(num1)) #Converted to Integer Data Type
print(type(num2)) #Converted to Integer Data Type

print("The max number between the two numbers is:", max(num1, num2))
print(f"The power of number 1 to the number 2 is: {pow(num1, num2):.4f}")

print(f"The sum of two numbers are: {num1+num2}")
print(f"The mul of two numbers are: {num1*num2}")
print(f"The sub of two numbers are: {num1-num2}")
print(f"The div of two numbers are: {num1/num2:.4f}")