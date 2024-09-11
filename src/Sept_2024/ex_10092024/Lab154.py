# try, except and finally
# file

import os

try:
    full_path = os.getcwd() # --> Current Working Directory
    full_path_file  = full_path + "/example.txt"
    print(full_path_file)

    print("************************")


    mkdirect = os.listdir()
    print(mkdirect)

    print("************************")

    file = open(full_path_file,'r') # FileNotFoundError: [Error 2] No such file or directory: 'example.txt'
    print(file.read())

except Exception as fnfe:
    print("File Not found, fix the path or create a file")

finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)