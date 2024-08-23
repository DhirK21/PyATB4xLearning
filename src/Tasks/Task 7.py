### Task #7
#✅ Leap Year Checker:

"""Create a program that determines whether a given year is a leap year.
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.

If a year is evenly divisible by 4, 100, and 400, then it is a leap year.
If a year is divisible by 4 but not by 100 and not divisible by 400, then it is also a leap year.
If a year is not divisible by 4, then it is not a leap"""

# Input the year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if year % 400 == 0:
    print(f"{year} is a leap year.")
elif year % 100 == 0:
    print(f"{year} is not a leap year.")
elif year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

