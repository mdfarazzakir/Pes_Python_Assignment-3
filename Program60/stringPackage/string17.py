"""
Strings:
Write a program to perform following operations on List. Create three lists as List1, List2 and List3 having 5 city names each list.

a. Find the length city of each list element and print city and length
b. Find the maximum and minimum string length element of each list
c. Compare each list and determine which city is biggest & smallest with length.
d. Delete first and last element of each list and print list contents.

"""
"""a)Function to find the length city of each list element and print city and length: List1"""
def CList1(List1):
    print("\nList1")
    for i in range(0,len(List1)):
        a = List1[i]
        b = len(a)
        c1.append(b)
        print("City %s with length %d"%(a,b))
    return(c1)

"""b)Function to find the maximum and minimum string length element of each list:- List1"""
def CL1MinMax(c1):
    lc = len(c1)
    s1 = c1[0]
    l1 = c1[lc-1]
    for j in range(len(c1)):
        if s1>c1[j]:
            s1=c1[j]

        if l1<c1[j]:
            l1=c1[j]
    print("\nList1")

    for k in range(len(c1)):
        if c1[k]==s1:
            print("\n",List1[k]," is the smallest city with length %d"%s1,"\n")
            aCity.append(List1[k])

        if c1[k]==l1:
            print("\n",List1[k]," is the largest city with length %d"%l1,"\n")
            aCity.append(List1[k])
    return(aCity)


"""a)Function to find the length city of each list element and print city and length:- List2"""
def CList2(List2):

    print("\nList2")
    for i in range(0,len(List2)):
        a = List2[i]
        b = len(a)
        c2.append(b)
        print("City %s with length %d"%(a,b))

"""b)Function to find the maximum and minimum string length element of each list:- List1"""
def CL2MinMax(c2):
    lc = len(c2)
    s2 = c2[0]
    l2 = c2[lc-1]
    for j in range(len(c2)):
        if s2>c2[j]:
            s2=c2[j]

        if l2<c2[j]:
            l2=c2[j]

    print("\nList2")
    for k in range(len(c2)):
        if c2[k]==s2:
            print("\n",List2[k]," is the smallest city with length %d"%s2,"\n")
            aCity.append(List2[k])

        if c2[k]==l2:
            print("\n",List2[k]," is the largest city with length %d"%l2,"\n")
            aCity.append(List2[k])


"""a)Function to find the length city of each list element and print city and length:- List3"""
def CList3(List3):

    print("\nList3")
    for i in range(0,len(List3)):
        a = List3[i]
        b = len(a)
        c3.append(b)
        print("City %s with length %d"%(a,b))
    return(c3)

"""b)Function to find the maximum and minimum string length element of each list:- List1"""
def CL3MinMax(c3):
    lc = len(c3)
    s3 = c3[0]
    l3 = c3[lc-1]
    for j in range(len(c3)):
        if s3>c3[j]:
            s3=c3[j]

        if l3<c3[j]:
            l3=c3[j]


    print("\nList3")

    for k in range(len(c3)):
        if c3[k]==s3:
            print("\n",List3[k]," is the smallest city with length %d"%s3)
            aCity.append(List3[k])

        if c3[k]==l3:
            print("\n",List3[k]," is the largest city with length %d"%l3,"\n")
            aCity.append(List3[k])

"""c)Function to compare each list and determine which city is biggest & smallest with length. """
def listComp(aCity):
    c = list()
    for i in range(0,len(aCity)):
        a = aCity[i]
        b = len(a)
        c.append(b)
    lc = len(c)
    s4 = c[0]
    l4 = c[lc-1]
    for j in range(len(c)):
        if s4>c[j]:
            s4=c[j]


        if l4<c[j]:
            l4=c[j]


    for k in range(len(c)):
        if c[k]==s4:
            print("\n",aCity[k]," is the smallest city with length %d"%s4)


        if c[k]==l4:
            print("\n",aCity[k]," is the largest city with length %d"%l4,"\n")


"""d)Function to delete first and last element of each list and print list contents."""
def newLists(List1,List2,List3):
    l1 = len(List1)
    l2 = len(List2)
    l3 = len(List3)

    nList1 = List1[0+1:l1-1]
    nList2 = List2[0+1:l2-1]
    nList3 = List3[0+1:l3-1]


    print("\nNew List1: ",nList1)
    print("\nNew List2: ",nList2)
    print("\nNew List3: ",nList3)




List1 = ['Kolkata','Mumbai','Chennai','Delhi','Bangalore']

List2 = ['New York City','Dallas','Detroit','New Orleans','Las Vages']

List3 = ['Barcelona','Madrid','Seville','Valencia','Granda']



aCity = list()
c1 = list()
c2 = list()
c3 = list()


print("a)Printing Cities and their lengths: ")
CList1(List1)
CList2(List2)
CList3(List3)

print("\nb)Printing maximum and minimum string length element of each list.")
CL1MinMax(c1)
CL2MinMax(c2)
CL3MinMax(c3)

print("\nc)Comparing each list to determine which city is biggest & smallest with length")
listComp(aCity)


print("\nd)After deleting first and last element of each list and printing the list contents")
newLists(List1,List2,List3)


# Output:
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program32.py
# a)Printing Cities and their lengths:
#
# List1
# City Kolkata with length 7
# City Mumbai with length 6
# City Chennai with length 7
# City Delhi with length 5
# City Bangalore with length 9
#
# List2
# City New York City with length 13
# City Dallas with length 6
# City Detroit with length 7
# City New Orleans with length 11
# City Las Vages with length 9
#
# List3
# City Barcelona with length 9
# City Madrid with length 6
# City Seville with length 7
# City Valencia with length 8
# City Granda with length 6
#
# b)Printing maximum and minimum string length element of each list.
#
# List1
#
#  Delhi  is the smallest city with length 5
#
#
#  Bangalore  is the largest city with length 9
#
#
# List2
#
#  New York City  is the largest city with length 13
#
#
#  Dallas  is the smallest city with length 6
#
#
# List3
#
#  Barcelona  is the largest city with length 9
#
#
#  Madrid  is the smallest city with length 6
#
#  Granda  is the smallest city with length 6
#
# c)Comparing each list to determine which city is biggest & smallest with length
#
#  Delhi  is the smallest city with length 5
#
#  New York City  is the largest city with length 13
#
#
# d)After deleting first and last element of each list and printing the list contents
#
# New List1:  ['Mumbai', 'Chennai', 'Delhi']
#
# New List2:  ['Dallas', 'Detroit', 'New Orleans']
#
# New List3:  ['Madrid', 'Seville', 'Valencia']
#
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
