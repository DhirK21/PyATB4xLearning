# File Handling

import os

full_path_file = os.path.join(r"C:\Users\Dhir\PycharmProjects\PyATB4xLearning\src\Sept_2024\ex_10092024", "dhir.txt")

file = open(full_path_file, 'r')
content = file.read()
print(content)

