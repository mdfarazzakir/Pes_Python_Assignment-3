"""
Strings:
Create 3 Lists (list1, list2, list3) with integer and perform following operations
a) Create Maxlist by taking 2 maximum elements from each list.
b) Find average value from all the elements of Maxlist.
c) Create a MinlIst by taking 2 minimum elements from each list
d) Find the average value from all the elements of Minlist

"""

"""Function to for List1"""
def List1(temp,l1,list1,Maxlist,Minlist):
    for i in range(0,l1):
        for j in range(0,l1):
            if list1[i]>list1[j]:
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
    Maxlist.append(list1[0])
    Maxlist.append(list1[1])
    Minlist.append(list1[l1-1])
    Minlist.append(list1[l1-2])
    return(Maxlist)
    return(Minlist)

"""Function to for List2"""
def List2(temp,l2,list2,Maxlist,Minlist):
    for i in range(0,l1):
        for j in range(0,l1):
            if list1[i]>list1[j]:
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
    Maxlist.append(list2[0])
    Maxlist.append(list2[1])
    Minlist.append(list2[l2-1])
    Minlist.append(list2[l2-2])
    return(Maxlist)
    return(Minlist)

"""Function to for List3"""
def List3(temp,l3,list3,Maxlist,Minlist):
    for i in range(0,l1):
        for j in range(0,l1):
            if list1[i]>list1[j]:
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
    Maxlist.append(list3[0])
    Maxlist.append(list3[1])
    Minlist.append(list3[l3-1])
    Minlist.append(list3[l3-2])
    return(Maxlist)
    return(Minlist)

"""Function to calculate average of Maxlist"""
def MaxmList(Maxlist):
    lm = len(Maxlist)
    sum = 0
    for i in range(0,lm):
        sum = sum+Maxlist[i]
    avg = sum/lm
    print("\nb) The average of all the elements of Maxlist is %d"%avg)

"""Function to calculate average of Minlist"""
def MinmList(Minlist):
    lm = len(Minlist)
    sum = 0
    for i in range(0,lm):
        sum = sum+Minlist[i]
    avg = sum/lm
    print("\nd) The average of all the elements of Minlist is %d"%avg)

"""Initializing the variables and the lists"""
Maxlist = list()
Minlist = list()
list1  = [52,354,345,35,2,36]
list2 = [645,795,2,674,687,574]
list3 = [746,125,167,746,854,965]


print("List1: ",list1,"\nList2: ",list2,"\nList3: ",list3)
l1 = len(list1)
l2 = len(list2)
l3 = len(list3)
temp = 0

"""Calling the Functions"""
List1(temp,l1,list1,Maxlist,Minlist)
List2(temp,l2,list2,Maxlist,Minlist)
List3(temp,l3,list3,Maxlist,Minlist)

"""a)Creation of Maxlist by taking 2 maximum elements from each list."""
print("\na)Printing Maxlist: ",Maxlist)

"""b) Finding the average value from all the elements of Maxlist."""
MaxmList(Maxlist)

"""c)Creation of Minlist by taking 2 minimum elements from each list."""
print("\nc)Printing Minlist:",Minlist)

"""d) Finding the average value from all the elements of Minlist."""
MinmList(Minlist)


# Output:
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program34.py
# List1:  [52, 354, 345, 35, 2, 36]
# List2:  [645, 795, 2, 674, 687, 574]
# List3:  [746, 125, 167, 746, 854, 965]
#
# a)Printing Maxlist:  [354, 345, 645, 795, 746, 125]
#
# b) The average of all the elements of Maxlist is 501
#
# c)Printing Minlist: [2, 35, 574, 687, 965, 854]
#
# d) The average of all the elements of Minlist is 519
#
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
