with open("dhir.txt", "r") as file:
    lines = file.readlines()
    
    for line in lines:
        print(line,end="")