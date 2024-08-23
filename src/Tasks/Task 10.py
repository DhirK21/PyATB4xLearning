# Task #10 -
# ✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

# factorial


number = int(input("enter the value of number:\n"))

if number < 0:
    print("factorial is not defined for negative numbers")

else:
    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial * i
        """
        factorial=1*1 -->1
        factorial=1*2-->2
        factorial=2*3-->6
        factorial=6*4-->24
        factorial=24*5-->120

        factorial=120

         """
    print(f"factorial of the given number {number} is {factorial}")