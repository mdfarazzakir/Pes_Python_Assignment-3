"""
Functions
Write function to extend the tuple with elements of list. Pass list and Tuple as parameter
to the function.
"""

"""Function to extend the tuple with elements of list"""

"""To pass the positional arguments in the function we have used *arg which acts as the representator for
 the arguments being input in the function"""
def tupExt(*arg):
    tuple1,list1 = arg
    tuple1 = list(tuple1)
    extTuple = tuple1 + list1
    print(tuple(extTuple))

"""Calling the function and passing tuple and list as parameters"""

tupExt((23,234.04,'Amazon',987,'Dalla'),[79.124,984,'Bengaluru','Hyderabad'])


# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>python Program47.py
# (23, 234.04, 'Amazon', 987, 'Dalla', 79.124, 984, 'Bengaluru', 'Hyderabad')

# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>