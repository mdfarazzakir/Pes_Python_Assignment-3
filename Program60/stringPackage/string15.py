"""
Strings:
Write a program to Sort given N numbers (Use only loop structures and Conditions to sort the elements.
Use Bubble sort / Selection sort technique to sort the elements of List) Note: Don't use built in functions to sort.

"""
"""Intializing the variable num as list"""
num = list()

"""Function to take numbers to be sorted as input"""
def numInput(num):


    lmt = int(input("Enter the limit for the list: "))

    for i in range(0,lmt):
        a = int(input("Enter the numbers: "))
        num.append(a)
    print("\nList of number being given as input: ",num)
    return(num)

"""Function for Bubble Sort"""
def bubbleSort(num):
    temp = 0
    for i in range(0,len(num)):
        for j in range(0,len(num)):
            if num[i]<num[j]:
                temp = num[i]
                num[i] = num[j]
                num[j] = temp

    print("\nList of sorting:",num)

"""Calling the functions"""
numInput(num)

bubbleSort(num)


# Output:
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program30.py
# Enter the limit for the list: 10
# Enter the numbers: 354
# Enter the numbers: 15
# Enter the numbers: 35
# Enter the numbers: 15
# Enter the numbers: 534
# Enter the numbers: 21
# Enter the numbers: 34
# Enter the numbers: 213
# Enter the numbers: 23453
# Enter the numbers: 15
#
# List of number being given as input:  [354, 15, 35, 15, 534, 21, 34, 213, 23453, 15]
#
# List of sorting: [15, 15, 15, 21, 34, 35, 213, 354, 534, 23453]
#
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
