"""
Strings:
Create Tuple as specified below;
a) Create a Tuple tup1 with days in a week & print the tuple elements
b) Create a Tuple tup2  with months in a year and concatenate it with tup1
c) Create 3 tuples( tup1,tup2,tup3) with numbers and determine which is greater.
d) Try to delete an individual element in tup1 and try deleting complete Tuple -tup1 notice the error type you get.
e) Insert new element in to tuple by typecasting it to List

"""

"""Function for finding the largest number"""
def tup(m1,m2,m3):
    print("\nc) Printing the greater number from all the three tuuples tup1, tup2, tup3")
    for i in range(0,l1):
        if tup1[i]>m1:
            m1 = tup1[i]
    print("\n%d is the greatest number in tup1"%m1)

    for j in range(0,l2):
        if tup2[j]>m2:
            m2 = tup2[j]
    print("\n%d is the greatest number in tup2"%m2)

    for k in range(0,l2):
        if tup3[k]>m3:
            m3 = tup3[k]
    print("\n%d is the greatest number in tup3"%m3)

"""Function for deleting"""
def tupDel(tup1,l1):
    print("\nd) tup1 tuple has a length of %d"%l1)
    pos = input("\ni)Enter the position from where you want to delete between 0 to %d: "%(l1-1))

    print("\nDeleting an element from tuple tup1")
    try:
        del(tup1[pos])
    except Exception as err:
        print("\nThe error type is:",err)

    print("\nii)Deleting tuple tup1")
    try:
        del(tup1)
        print("\nDeletion successful")
    except Exception as err:
        print("\nThe error type is:",err)


"""Function for inserting new element"""
def tupInsertElm(tup1):
    print("\ne) Element insertion in tuple: ")
    print("Before insertion: ",tup1)
    elm = eval(input("Enter the number you want to enter: "))
    list1 = list(tup1)
    list1.append(elm)
    tup1 = tuple(list1)
    print("Element insertion successful",tup1)


"""a) Creating a Tuple tup1 with days in a week & printing the tuple elements"""
tup1 = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
print("\na)Print tuple tup1 with days in a week:\n",tup1)


"""b) Creating a Tuple tup2 with months in a year & printing the tuple elements"""
tup2 = ('January','February','March','April','May','June','July','August','September','October','November','December')
print("\nb)Print tuple tup2 with days in a week:\n",tup2)


"""c) Creating 3 tuples( tup1,tup2,tup3) with numbers and determining which is greater."""

tup1  = (52,354,345,35,2,36)
tup2 =(645,795,2,674,687,574)
tup3 = (746,125,167,746,854,965)

l1 = len(tup1)
l2 = len(tup2)
l3 = len(tup3)

m1 = tup1[l1-1]
m2 = tup2[l2-1]
m3 = tup3[l3-1]




tup(m1,m2,m3)

"""d) Deleting an individual element in tup1 and trying to delete complete Tuple"""

tupDel(tup1,l1)


"""e) Inserting new element in to tuple by typecasting it to List."""
tupInsertElm(tup1)



# Output:
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program35.py
#
# a)Print tuple tup1 with days in a week:
#  ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
#
# b)Print tuple tup2 with days in a week:
#  ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
#
# c) Printing the greater number from all the three tuuples tup1, tup2, tup3
#
# 354 is the greatest number in tup1
#
# 795 is the greatest number in tup2
#
# 965 is the greatest number in tup3
#
# d) tup1 tuple has a length of 6
#
# i)Enter the position from where you want to delete between 0 to 5: 4
#
# Deleting an element from tuple tup1
#
# The error type is: 'tuple' object does not support item deletion
#
# ii)Deleting tuple tup1
#
# Deletion successful
#
# e) Element insertion in tuple:
# Before insertion:  (52, 354, 345, 35, 2, 36)
# Enter the number you want to enter: 254
# Element insertion successful (52, 354, 345, 35, 2, 36, 254)
#
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
