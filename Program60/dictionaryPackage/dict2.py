"""
Dictionary  and Date & Time:

Create 2 dictionaries as follows:
dict1 ={'Name':'Ramakrishna','Age':25}
dict2={'EmpId':1234,'Salary':5000}

Perform following operations:  
a) Create single dictionary by merging dict1 and dict2
b) Update the salary to 10%
c) Update the age to 26
d) Insert the new element with key "grade" and assign value as "B1"
e) Extract and print all values and keys separately.
f) delete the element with key 'Age' and print dictionary elements.

"""
def dictionary():
    dict1 = dict(Name='Ramakrishna',Age=25)
    dict2 = dict(EmpId=1234,Salary=5000)

    """a) Create single dictionary by merging dict1 and dict2"""
    dictN = {**dict1,**dict2}
    print("\na)After merging dict1 and dict2 we get dictN: ",dictN)

    """b) Update the salary to 10%"""
    print("\nb)Salary before updation: ",dictN['Salary'])
    nSal = (10/100)*dictN['Salary']
    dictN.update(Salary=dictN['Salary']+nSal)
    print("\nSalary after updation: ",dictN['Salary'])

    """c) Update the age to 26"""
    print("\nc)Age before updation: ",dictN['Age'])
    nAge = 26
    dictN.update(Age=nAge)
    print("\nAge after updation: ",dictN['Age'])

    """d) Insert the new element with key "grade" and assign value as "B1"""
    print("\nd)dictN: ",dictN)
    dictN.update(grade = 'B1')
    print("\nUpdated dictN: ",dictN)

    """e) Extract and print all values and keys separately."""
    print("\ne)Extracting keys and values seperately and printing them")
    for key in dictN:
        print("\nKeys: ",key,end="")
    print("\n")
    for key in dictN:
        print("\nValues: ",dictN[key],end="")
    print("\n")
    """f) delete the element with key 'Age' and print dictionary elements."""
    print("\nf)Deleting the element with key 'Age'")
    del(dictN['Age'])
    print("\nUpdated dictN: ",dictN)

dictionary()


# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program38.py
#
# a)After merging dict1 and dict2 we get dictN:  {'Name': 'Ramakrishna', 'Age': 25, 'EmpId': 1234, 'Salary': 5000}
#
# b)Salary before updation:  5000
#
# Salary after updation:  5500.0
#
# c)Age before updation:  25
#
# Age after updation:  26
#
# d)dictN:  {'Name': 'Ramakrishna', 'Age': 26, 'EmpId': 1234, 'Salary': 5500.0}
#
# Updated dictN:  {'Name': 'Ramakrishna', 'Age': 26, 'EmpId': 1234, 'Salary': 5500.0, 'grade': 'B1'}
#
# e)Extracting keys and values seperately and printing them
#
# Keys:  Name
# Keys:  Age
# Keys:  EmpId
# Keys:  Salary
# Keys:  grade
#
#
# Values:  Ramakrishna
# Values:  26
# Values:  1234
# Values:  5500.0
# Values:  B1
#
#
# f)Deleting the element with key 'Age'
#
# Updated dictN:  {'Name': 'Ramakrishna', 'EmpId': 1234, 'Salary': 5500.0, 'grade': 'B1'}
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
