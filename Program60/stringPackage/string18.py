"""
Strings:

Create a list with 7 elements and perform following operations. Let the list be initialized with List1 any 5 city names;
a) Append a new city name to the List
b) Insert a city name at 4th index position
c) Sort the list and print all elements
d) Sort the elements of the list in descending order.
e) delete last three elements using pop operation

"""
def addingCity(List1):
    print("a) Appending a new city in the list")
    nc = input("\nEnter the city name you want to add: ")
    print("\nList before appending: ",List1)
    List1.append(nc)
    print("\nNew city appended: ",List1)
    return(List1)


def insertAT4th(List1):
    print("\nb) Inserting a new city at 4th position in the lis")
    nc4 = input("\nEnter the city name you to insert at 4th position: ")
    print("\nList before adding at position 4: ",List1)
    List1.insert(4-1,nc4)
    print("\nAfter adding at 4th position: ",List1)
    return(List1)


def listSort(List1):
    print("\nc)Sorting the list: ")
    temp = str()
    for i in range(len(List1)):
        for j in range(len(List1)):
            if List1[i]<List1[j]:
                temp = List1[i]
                List1[i] = List1[j]
                List1[j] = temp
    print(List1)
    return(List1)
#
def listSortD(List1):
    print("\nd)Sorting the list in descending order: ")
    temp = str()
    for i in range(len(List1)):
        for j in range(len(List1)):
            if List1[i]>List1[j]:
                temp = List1[i]
                List1[i] = List1[j]
                List1[j] = temp
    print(List1)
    return(List1)


def popOp(List1):
    print("\ne)Poping last three elements: ")
    l = len(List1)
    count = 0
    i = l
    while True:
        popval = List1[i-1]
        print("\nPoping from the end of the list: ",popval)
        List1 = List1[:i-1]
        i -= 1
        count +=1
        if count == 3:
            break
    print("\n3 values from the end of the list has been poped and the list vallue now is: ",List1)


List1 = ['Kolkata','Bangalore','Mumbai','Chennai','Pune']


addingCity(List1)
insertAT4th(List1)
listSort(List1)
listSortD(List1)
popOp(List1)



# Output:
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program33.py
# a) Appending a new city in the list
#
# Enter the city name you want to add: Madrid
#
# List before appending:  ['Kolkata', 'Bangalore', 'Mumbai', 'Chennai', 'Pune']
#
# New city appended:  ['Kolkata', 'Bangalore', 'Mumbai', 'Chennai', 'Pune', 'Madrid']
#
# b) Inserting a new city at 4th position in the lis
#
# Enter the city name you to insert at 4th position: Oklahoma
#
# List before adding at position 4:  ['Kolkata', 'Bangalore', 'Mumbai', 'Chennai', 'Pune', 'Madrid']
#
# After adding at 4th position:  ['Kolkata', 'Bangalore', 'Mumbai', 'Oklahoma', 'Chennai', 'Pune', 'Madrid']
#
# c)Sorting the list:
# ['Bangalore', 'Chennai', 'Kolkata', 'Madrid', 'Mumbai', 'Oklahoma', 'Pune']
#
# d)Sorting the list in descending order:
# ['Pune', 'Oklahoma', 'Mumbai', 'Madrid', 'Kolkata', 'Chennai', 'Bangalore']
#
# e)Poping last three elements:
#
# Poping from the end of the list:  Bangalore
#
# Poping from the end of the list:  Chennai
#
# Poping from the end of the list:  Kolkata
#
# 3 values from the end of the list has been poped and the list vallue now is:  ['Pune', 'Oklahoma', 'Mumbai', 'Madrid']
#
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
