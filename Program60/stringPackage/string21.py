"""
Strings:
Create two tuples tup1 & tup2 and apply all built in functions on tuples. ( Refer Tutorial for the Built in functions list)

"""

"""Finding tupe length usin len(tuple)"""
def length(tup1,tup2):
    l1 = len(tup1)
    l2 = len(tup2)
    print("\nLength of tup1 is %d and length of tup2 %d"%(l1,l2))

"""Finding the minimum and maximum element in the tuple"""
def MinMax(tup1):
    minm = min(tup1)
    maxm = max(tup1)
    print("\n%d is the maximum value and %d is the minimum value in tuple tup1"%(maxm,minm))

"""Converting list to tuple using tuple()"""
def convert(tup1):
    print("\nThe type of tup1 is ",type(tup1))

    tup1 = list(tup1)

    print("\nAfter converting tuple to list")
    print("\nChecking the type of tup1: ",type(tup1))

"""Assigning values to tuples"""
tup1 = (1,4,3,5,2,7)
tup2 = (5,3,6,3,7,87)

"""Calling the Function"""

length(tup1,tup2)

MinMax(tup1)

convert(tup1)


# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program36.py
#
# Length of tup1 is 6 and length of tup2 6
#
# 7 is the maximum value and 1 is the minimum value in tuple tup1
#
# The type of tup1 is  <class 'tuple'>
#
# After converting tuple to list
#
# Checking the type of tup1:  <class 'list'>
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
