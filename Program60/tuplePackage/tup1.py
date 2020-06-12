
"""
Basic of Tuple:

Repeat program 7 with Tuples (Take example from Tutorial)

"""

"""Printing the elements of the tuples"""
def elmtPrint(tup1):
    print("\nTuple1:\n",tup1)
    print("\nTuple2\n",tup2)

"""Tuple Slicing"""
def slicing(tup1):
    l1 = len(tup1)
    print("\n",tup1[:(l1//2)],"is the first half of the Tuple1.\n")
    print(tup1[(l1//2):],"is the second half of the Tuple1.\n")

"""Repeating the elements of the tuple"""
def repeat(tup1):
    rt = input("Enter the number of times you want to repeat the tuple:")
    print("Repeating the Tuple1: \n",tup1*10)

"""Concatenating two tuples"""
def concat(tup1,tup2):
    print("\nTuple concatenation: Tuple1+Tuple2\n",tup1+tup2)


"""First tuple input"""
tup1 = input("Enter minimum 10 number for the tuple:").split()

"""Converting the strings to integers"""
for i in range(len(tup1)):
    tup1[i] = int(tup1[i])
tup1 = tuple(tup1)

"""Second tuple input"""
tup2 = input("Enter the tuple for concatenation:").split()

"""Converting the strings to integers"""
for i in range(len(tup2)):
    tup2[i] = int(tup2[i])
tup2 = tuple(tup2)


"""Calling the fucntions"""
elmtPrint(tup1)

slicing(tup1)

repeat(tup1)

concat(tup1,tup2)


#Output:
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-1>python Program8.py
#
# Enter minimum 10 number for the tuple:1 2 3 4 5 6 7 8 9 10
# Enter the tuple for concatenation:10 9 8 7 6 5 4 3 2 1
#
# Tuple1:
#  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# Tuple2
#  (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
#
#  (1, 2, 3, 4, 5) is the first half of the Tuple1.
#
# (6, 7, 8, 9, 10) is the second half of the Tuple1.
#
# Enter the number of times you want to repeat the tuple:5
# Repeating the Tuple1:
#  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#  10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8,
#  9, 10)
#
# Tuple concatenation: Tuple1+Tuple2
#  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
#
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-1>
