"""
Python List functions and Methods

Create a list of 5 names and check given name exist in the List.
        a) Use membership operator (IN) to check the presence of an element.
        b) Perform above task without using membership operator.
        c) Print the elements of the list in reverse direction.

"""

l = ['Frank','Murray','Arthur','Fleck','Gotham']

"""a) Checking the presence of element in the list using IN operator"""
print("a) Using membership operator (IN) to check the presence of an element.")
ckName = input('\nEnter the name you want to check in the list: ')

if ckName in l:
    # pos = [i for i in range(0,len(l))]
    print("\nThe name ",ckName," is present in the list at position :",l.index(ckName))
else:
    print("\nThe name is not present.")

"""b) Checking the presence of element in the list without IN operator"""
print("\nb) Performing above task a) without using membership operator.")

ckName = input('\nEnter the name you want to check in the list: ')
count=0
for i in range(0,len(l)):
    if l[i]==ckName:
        print("\nThe name",ckName,"is present in the list at position ",l.index(ckName))


    # if count==1:
    #     print("\nThe name is not present.")

print("\nList before reversing: ",l)
print("\nPrinting the elements of the list in reverse direction.")
rl = [l[i] for i in range(len(l)-1,-1,-1)]
print("\n",rl)

# Output:
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-1>python Program15.py
# a) Using membership operator (IN) to check the presence of an element.
#
# Enter the name you want to check in the list: Frank
#
# The name  Frank  is present in the list at position : 0
#
# b) Performing above task a) without using membership operator.
#
# Enter the name you want to check in the list: Arthur
#
# The name Arthur is present in the list at position  2
#
# The name is not present.
#
# List before reversing:  ['Frank', 'Murray', 'Arthur', 'Fleck', 'Gotham']
#
# Printing the elements of the list in reverse direction.
#
# ['Gotham', 'Fleck', 'Arthur', 'Murray', 'Frank']
#
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-1>
