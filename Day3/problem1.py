'''
Create a program that takes a year as input and checks if
it is a leap year or not

'''

year = int(input("Enter the year: "))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("Year is leap year")
        else:
            print("Year is not leap year")
    else:
        print("Year is leap year")
else:
    print("Year is not leap year")
