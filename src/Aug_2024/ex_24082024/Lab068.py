# Create a program to sum of three number from the user input

num1 = int(input("Enter the the number 1:")) # 100
num2 = int(input("Enter the the number 2:")) # 200
num3 = int(input("Enter the the number 3:")) # 300


def sum_of_three_number(n1=num1, n2=num2, n3=num3):
    return n1 + n2 + n3


result = sum_of_three_number()
print(result)