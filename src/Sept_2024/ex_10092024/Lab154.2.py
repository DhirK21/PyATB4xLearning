import os

try:
    file = open(r'C:\Users\Dhir\PycharmProjects\PyATB4xLearning\src\Sept_2024\ex_10092024\example.txt', 'r') # By adding r before the file path, the string is treated as a raw string, and backslashes are not interpreted as escape characters.
    print(file.read())

except FileNotFoundError as fnfe:
    print("File Not Found, fix the path or create new file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)