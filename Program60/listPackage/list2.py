"""
Python List functions and Methods:

Write a program to create two list A & B such that List A contains Employee Id, List B contain Employee name (minimum 10 entries in each list) & perform following operation
     a) Print all names on to screen
     b) Read the index from the  user and print the corresponding name from both list.
     c) Print the names from 4th position to 9th position
     d) Print all names from 3rd position till end of the list
     e) Repeat list elements by specified number of times (N- times, where N is entered by user)
     f) Concatenate two lists and print the output.
     g) Print element of list A and B side by side.(i.e. List-A First element, List-B First element )

"""
"""Input number of entries"""
eCount = int(input("Enter the number of entries, minimum 10 entries should be given: "))

"""Input Employess Ids"""
A_EmpId = [int(input("\nEnter Employee Id %d: "%i)) for i in range(1,eCount+1)]

"""Input Employee Names"""
B_EmpName = [input("\nEnter Employee Name against Id %d: "%A_EmpId[i]) for i in range(0,eCount)]

"""a) Printing list of Employee"""
print("\n\na) List of Employee Names: ",B_EmpName)

"""Input entry number"""
ind = int(input("\n\nb) Give any entry number from 0 to %d to get the details: "%(eCount-1)))

"""b)PrintingEmployee details"""
print("\nThe Employee Id is %d and Employee Name is %s"%(A_EmpId[ind],B_EmpName[ind]))

"""C)Printing Employee Name from position 4 to position 9"""
pos4to9 = [B_EmpName[i] for i in range(4-1,9-1)]

print("\n\nc) Employess from 4th position to 9th position are: ",pos4to9)

"""d)Printing Employee Name from position 3 till the end"""
pos3tillend = [B_EmpName[i] for i in range(3-1,eCount)]

print("\n\nd) Employess from 3rd position till the end are: ",pos3tillend)

"""e)Repeating list elements for N time"""
repeat = int(input("\nEnter the number of times the list elements are to be repeated: "))
print("\n\ne) Repeating lists:\n",A_EmpId*repeat, B_EmpName*repeat)

"""f)Concatenating two lists"""
C_Emp = list()
C_Emp = A_EmpId + B_EmpName

print("\n\nf)List after concatenation:",C_Emp)

"""g)Print element of list A and B side by side."""
print("\n\ng)Printing Employee id and Employee Name side by side")
for i in range(0,eCount):
    print(A_EmpId[i],B_EmpName[i])

# Output:
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-1>python Program14.py
# Enter the number of entries, minimum 10 entries should be given: 10
#
# Enter Employee Id 1: 001
#
# Enter Employee Id 2: 002
#
# Enter Employee Id 3: 003
#
# Enter Employee Id 4: 004
#
# Enter Employee Id 5: 005
#
# Enter Employee Id 6: 006
#
# Enter Employee Id 7: 007
#
# Enter Employee Id 8: 008
#
# Enter Employee Id 9: 009
#
# Enter Employee Id 10: 010
#
# Enter Employee Name against Id 1: Arthur
#
# Enter Employee Name against Id 2: Frank
#
# Enter Employee Name against Id 3: Thomas
#
# Enter Employee Name against Id 4: Bruce
#
# Enter Employee Name against Id 5: Martha
#
# Enter Employee Name against Id 6: Harley
#
# Enter Employee Name against Id 7: Jason
#
# Enter Employee Name against Id 8: Dick
#
# Enter Employee Name against Id 9: Barbara
#
# Enter Employee Name against Id 10: Kate
#
#
# a) List of Employee Names:  ['Arthur', 'Frank', 'Thomas', 'Bruce', 'Martha', 'Harley', 'Jason', 'Dick', 'Barbara', 'Kate']
#
#
# b) Give any entry number from 0 to 9 to get the details: 4
#
# The Employee Id is 5 and Employee Name is Martha
#
#
# c) Employess from 4th position to 9th position are:  ['Bruce', 'Martha', 'Harley', 'Jason', 'Dick']
#
#
# d) Employess from 3rd position till the end are:  ['Thomas', 'Bruce', 'Martha', 'Harley', 'Jason', 'Dick', 'Barbara', 'Kate']
#
# Enter the number of times the list elements are to be repeated: 5
#
#
# e) Repeating lists:
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ['Arthur', 'Frank', 'Thomas', 'Bruce', 'Martha', 'Harley', 'Jason', 'Dick', 'Barbara', 'Kate', 'Arthur', 'Frank', 'Thomas', 'Bruce', 'Martha', 'Harley', 'Jason', 'Dick', 'Barbara', 'Kate', 'Arthur', 'Frank', 'Thomas', 'Bruce', 'Martha', 'Harley', 'Jason', 'Dick', 'Barbara', 'Kate', 'Arthur', 'Frank', 'Thomas', 'Bruce', 'Martha', 'Harley', 'Jason', 'Dick', 'Barbara', 'Kate', 'Arthur', 'Frank', 'Thomas', 'Bruce', 'Martha', 'Harley', 'Jason', 'Dick', 'Barbara', 'Kate']
#
#
# f)List after concatenation: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Arthur', 'Frank', 'Thomas', 'Bruce', 'Martha', 'Harley', 'Jason', 'Dick', 'Barbara', 'Kate']
#
#
# g)Printing Employee id and Employee Name side by side
# 1 Arthur
# 2 Frank
# 3 Thomas
# 4 Bruce
# 5 Martha
# 6 Harley
# 7 Jason
# 8 Dick
# 9 Barbara
# 10 Kate
#
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-1>
