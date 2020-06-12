"""
Dictionary  and Date & Time:
Using calendar module perform following operations.
a) Print the 2016 calendar with space between months as 10 characters.
b) How many leap days between the years 1980 to 2025.
c) Check given year is leap year or not. 
d) print calendar of any specified month of the year 2016.

"""
"""Importing the Claendar library"""
import calendar as cl

"""Function to generate months of the year 2016"""
def mnths():
    """Using try and except block for error handling"""
    try:
        months = cl.calendar(2016,c=10)
        print(months)

    except:
        print("Error encountered, please recheck the code")

mnths()


# Output:
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program41a.py
#                                       2016

#       January                       February                       March
# Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su
#              1  2  3           1  2  3  4  5  6  7              1  2  3  4  5  6
#  4  5  6  7  8  9 10           8  9 10 11 12 13 14           7  8  9 10 11 12 13
# 11 12 13 14 15 16 17          15 16 17 18 19 20 21          14 15 16 17 18 19 20
# 18 19 20 21 22 23 24          22 23 24 25 26 27 28          21 22 23 24 25 26 27
# 25 26 27 28 29 30 31          29                            28 29 30 31

#        April                          May                           June
# Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su
#              1  2  3                             1                 1  2  3  4  5
#  4  5  6  7  8  9 10           2  3  4  5  6  7  8           6  7  8  9 10 11 12
# 11 12 13 14 15 16 17           9 10 11 12 13 14 15          13 14 15 16 17 18 19
# 18 19 20 21 22 23 24          16 17 18 19 20 21 22          20 21 22 23 24 25 26
# 25 26 27 28 29 30             23 24 25 26 27 28 29          27 28 29 30
#                               30 31

#         July                         August                      September
# Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su
#              1  2  3           1  2  3  4  5  6  7                    1  2  3  4
#  4  5  6  7  8  9 10           8  9 10 11 12 13 14           5  6  7  8  9 10 11
# 11 12 13 14 15 16 17          15 16 17 18 19 20 21          12 13 14 15 16 17 18
# 18 19 20 21 22 23 24          22 23 24 25 26 27 28          19 20 21 22 23 24 25
# 25 26 27 28 29 30 31          29 30 31                      26 27 28 29 30

#       October                       November                      December
# Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su
#                 1  2              1  2  3  4  5  6                    1  2  3  4
#  3  4  5  6  7  8  9           7  8  9 10 11 12 13           5  6  7  8  9 10 11
# 10 11 12 13 14 15 16          14 15 16 17 18 19 20          12 13 14 15 16 17 18
# 17 18 19 20 21 22 23          21 22 23 24 25 26 27          19 20 21 22 23 24 25
# 24 25 26 27 28 29 30          28 29 30                      26 27 28 29 30 31
# 31

# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$