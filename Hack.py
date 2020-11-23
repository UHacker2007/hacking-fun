print("Hacker2007")
print("black hat hacker")
input('What is your name?')
# Python Program - Get String Input from User
str = input("Enter any string: ")
print(str)
# User enters the year
year = int(input("Enter Year: "))
# Leap Year Check
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
