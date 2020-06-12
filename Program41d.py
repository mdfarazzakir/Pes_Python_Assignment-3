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
    month2016 = eval(input("Enter the month number of the year 2016 you want to print: "))
    month = cl.month(2016,month2016)

    print("The month is:-",month)
except:
    print("Invalid input, please try again")


# Output:
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program41d.py
# Enter the month number of the year 2016 you want to print: 2016
# Invalid input, please try again
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program41d.py
# Enter the month number of the year 2016 you want to print: 5
# The month is:-       May 2016
# Mo Tu We Th Fr Sa Su
#                    1
#  2  3  4  5  6  7  8
#  9 10 11 12 13 14 15
# 16 17 18 19 20 21 22
# 23 24 25 26 27 28 29
# 30 31

# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program41d.py
# Enter the month number of the year 2016 you want to print: 7
# The month is:-      July 2016
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31

# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$