"""
Dictionary  and Date & Time :
Using Time and Calendar module, Print current date and time. Print current month calendar.

"""
import datetime as dt

import calendar as cl

ct = dt.datetime.now()


print("The current date and time is as follows: ")

print("The time is: ",ct.hour," hours ",ct.minute,"minutes and ",ct.second,"seconds")

cm = cl.month(2020,5)

print("\nThe month calendar is: ",cm)

# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program39.py
# The current date and time is as follows:
# The time is:  17  hours  5 minutes and  59 seconds
#
# The month calendar is:        May 2020
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31
#
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
