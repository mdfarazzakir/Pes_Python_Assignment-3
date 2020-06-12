"""
Basic LIST Operations :

Create a list with at least 10 elements having integer values in it;
       Print all elements
       Perform slicing operations
       Perform repetition with * operator
       Perform concatenation with other list.

"""
"""Printing the elements of the Lists"""
def elmtPrint(list1):
    print("\nList1:\n",list1)
    print("\nList2\n",list2)

"""List Slicing"""
def slicing(list1):
    l1 = len(list1)
    print("\n",list1[:(l1//2)],"is the first half of the List1.\n")
    print(list1[(l1//2):],"is the second half of the List1.\n")

"""Repeating the elements of the list"""
def repeat(list1):
    rt = input("Enter the number of times you want to repeat the list:")
    print("Repeating the List1: \n",list1*10)

"""Concatenating two lists"""
def concat(list1,list2):
    print("\nList concatenation: List1+List2\n",list1+list2)



"""First list input"""
list1 = input("Enter minimum 10 numbers for the list:").split()

"""Converting the strings to integers"""
for i in range(len(list1)):
    list1[i] = int(list1[i])

"""Second list input"""
list2 = input("Enter the list for concatenation:").split()

"""Converting the strings to integers"""
for i in range(len(list2)):
    list2[i] = int(list2[i])


"""Calling the fucntions"""
elmtPrint(list1)

slicing(list1)

repeat(list1)

concat(list1,list2)

#Output:
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-1>python Program7.py
#
# Enter minimum 10 numbers for the list:1 2 3 4 5 6 7 8 9 10
# Enter the list for concatenation:10 9 8 7 6 5 4 3 2 1
#
# List1:
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# List2
#  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#
#  [1, 2, 3, 4, 5] is the first half of the List1.
#
# [6, 7, 8, 9, 10] is the second half of the List1.
#
# Enter the number of times you want to repeat the list:5
# Repeating the List1:
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#  10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8,
#  9, 10]
#
# List concatenation: List1+List2
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-1>
