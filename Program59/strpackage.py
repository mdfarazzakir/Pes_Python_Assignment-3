"""
Modules & Packages:
Create file called "stringop.py" which has following functions
i) functions to sort numbers (Use loops for  sorting, do not use built in function)
ii) function to search given element through binary search method.(Refer to net for the Binary search algorithm)
iii) function to reverse the given string 
Write new program in file strpackage.py such that you import functions of file "stringop.py" to your new program
"""
"""For all the different types of operation the functions have been imported exclusively from stringop.py file"""

"""Sorting number using bubble sort"""
from stringop import bubbleSort

print("i)Bubble Sorting the number list [57,54,567,168,435,4,58,468,542,554]")
print(bubbleSort([57,54,567,168,435,4,58,468,542,554]))

"""Binary Search"""
from stringop import binarySearch
sortedList = [4, 54, 57, 58, 168, 435, 468, 542, 554, 567]
lower = 0
upper = len(sortedList)-1
numberTosearch = int(input("\nii)Enter the number you want to search from the list [4, 54, 57, 58, 168, 435, 468, 542, 554, 567]: "))
print("Binary Search")
if binarySearch(sortedList,lower,upper,numberTosearch)==0:
    print("Number not found")
else:
    print("Number found at position",binarySearch(sortedList,lower,upper,numberTosearch)+1)

"""Reversing the string"""
from stringop import strgReverse
strg = 'Bengaluru'
print("\niii)String reversal")
print("%s after reversal is %s"%(strg,strgReverse(strg)))


# Output:
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3\Program59>python strpackage.py
# i)Bubble Sorting the number list [57,54,567,168,435,4,58,468,542,554]
# [4, 54, 57, 58, 168, 435, 468, 542, 554, 567]

# ii)Enter the number you want to search from the list [4, 54, 57, 58, 168, 435, 468, 542, 554, 567]: 435
# Binary Search
# Number found at position 6

# iii)String reversal
# Bengaluru after reversal is urulagneB

# C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3\Program59>