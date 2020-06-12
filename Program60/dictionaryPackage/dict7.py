"""
Dictionary  and Date & Time:
Using calendar module perform following operations.
a) Print the 2016 calendar with space between months as 10 characters.
b) How many leap days between the years 1980 to 2025.
c) Check given year is leap year or not. 
d) print calendar of any specified month of the year 2016.

"""
"""Importing the calender module"""
import calendar as cl

"""Requirment is to calculate the number of leap days between the years 1980 to 2025, so stating the limit"""
yearFrom = 1980
yearTill = 2025

"""Using the leapDays() method to get the number of leap days"""
leapDays = cl.leapdays(yearFrom,yearTill)
print("Total number of leap days is %d between 1980 and 2025"%leapDays)


# Output:
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program41b.py 
# Total number of leap days is 12 between 1980 and 2025