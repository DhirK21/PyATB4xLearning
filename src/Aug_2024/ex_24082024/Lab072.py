def print_arguments(*args):
    # *args = multiple argument with no limit, -> list
    # print(args[0])
    for i in args:
        print(i, end=' ')
    print() # Move to the next line after printing all the arguments

# list = ["dhir", "amit", "lucky"]
print("*****************")
print_arguments("dhir", "amit", "lucky")
print_arguments("amit", "lucky",)
print_arguments("amit", 10)
print_arguments("amit", 10, True)
print_arguments("amit", 10, True, False)
print_arguments("amit", 10, True, False, "DHIR")
print_arguments("lucky")
# print_arguments() -minimum 1 arguement is importa

print("******************")
print("amit")
print("dhir", "amit")
print("dhir", "amit", True)
print("dhir", "amit", True, False)