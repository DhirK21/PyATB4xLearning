#Task #11 -
# ✅ Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

num = int(input("Enter the number for the Fibonacci series: "))
a,b = 0,1

print("Fibonacci series")

count = 0

while count <= num:
    print(a, end =" ")

    a,b=b,a+b
    """
    a,b=0,1
    a,b=1,1
    a,b=1,2
    a,b=2,3
    a,b=3,5
    a,b=5,8
    a,b=8,13
    """
    count=count+1