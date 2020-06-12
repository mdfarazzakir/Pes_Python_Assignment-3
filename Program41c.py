"""
Dictionary  and Date & Time:
Using calendar module perform following operations.
a) Print the 2016 calendar with space between months as 10 characters.
b) How many leap days between the years 1980 to 2025.
c) Check given year is leap year or not. 
d) print calendar of any specified month of the year 2016.

"""
"""Importing calendar library"""
import calendar as cl


"""Using try and except block for error handling"""
try:
    """Taking year as input to check if the given year is a leap year or not"""
    year = eval(input("Enter the year you want to check: "))
    if cl.isleap(year)==True:
        print("%d is a leap year"%year)
    else:
        print("%d is not a leap year"%year)
except:
    print("Invalid input, please try again.")


# Output:
# golem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program41c.py 
# Enter the year you want to check: fdwa
# Invalid input, please try again.
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program41c.py 
# Enter the year you want to check: 2016
# 2016 is a leap year
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program41c.py 
# Enter the year you want to check: 5874
# 5874 is not a leap year
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program41c.py 
# Enter the year you want to check: 2018
# 2018 is not a leap year
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$