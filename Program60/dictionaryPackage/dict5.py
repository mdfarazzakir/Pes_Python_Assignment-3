"""
Dictionary  and Date & Time:
Using time module perform following operations.
b) Write a program to find out how much CPU time is taken for the execution of above(32.a)  program.
"""
import time

""""b)Program to find out how much CPU time is taken for the execution of above(32.a)  program"""
start_time = time.time()


def CList1(List1):
    print("\nList1")
    for i in range(0,len(List1)):
        a = List1[i]
        b = len(a)
        c1.append(b)
        print("City %s with length %d"%(a,b))
    return(c1)


def CList2(List2):

    print("\nList2")
    for i in range(0,len(List2)):
        a = List2[i]
        b = len(a)
        c2.append(b)
        print("City %s with length %d"%(a,b))

def CList3(List3):

    print("\nList3")
    for i in range(0,len(List3)):
        a = List3[i]
        b = len(a)
        c3.append(b)
        print("City %s with length %d"%(a,b))
    return(c3)


List1 = ['Kolkata','Mumbai','Chennai','Delhi','Bangalore']

List2 = ['New York City','Dallas','Detroit','New Orleans','Las Vages']

List3 = ['Barcelona','Madrid','Seville','Valencia','Granda']

c1 = list()
c2 = list()
c3 = list()

CList1(List1)
CList2(List2)
CList3(List3)


print("\nb) Time taken to execute program 32a is %s seconds" % (time.time() - start_time))


# Output:
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
# b) Time taken to execute program 32a is 0.0010004043579101562 seconds
