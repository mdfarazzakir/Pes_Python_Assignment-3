"""
Strings:
Write a program to search an element in the list. i.e. Perform the binary search on the sorted list having integers as elements.
If the search is successful print "Success" else print "un successful search".

"""
"""Binary Search Function"""
def bs(st,l,u,Sortedlist):
    while l <= u:
        m = (l+u)//2
        if Sortedlist[m]==st:
            return m
        elif Sortedlist[m]<st:
            l = m+1
        else:
            u = m-1
    return(0)

"""Inputs"""
Sortedlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lt = len(Sortedlist)
l = 0
u = lt-1
st = int(input("Enter the search term "))

"""Calling the Function"""
res = bs(st,l,u,Sortedlist)

if res == 0:
    print("Unsuccessful")
else:
    print("Successful")


# Output:
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program31.py
# Enter the search term 5
# Successful
#
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program31.py
# Enter the search term 21
# Unsuccessful
#
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
