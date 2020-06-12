"""
Dictionary  and Date & Time:
Create 3 dictionaries (dict1, dict2, dict3) with 3 elements each. Perform following operations
a) Compare dictionaries to determine the biggest.
b) Add new elements in to the dictionaries dict1, dict2
c) print the length of dict1, dict2, dict3.
d) Convert dict1, dict2, and dict3 dictionaries as string and concatenate all strings together.

"""
"""Function to compare all the three dictionaries."""
def compare(dict1,dict2,dict3):
    print("\na)Result after comparison: ")
    d1c = 0
    d2c = 0
    d3c = 0
    for key1 in dict1:
        for key2 in dict2:
            if dict1[key1]> dict2[key2]:
                d1c +=1
            elif dict1[key1]< dict2[key2]:
                d2c +=1
            else:
                continue

    for key1 in dict1:
        for key3 in dict3:
            if dict1[key1]> dict3[key3]:
                d1c +=1
            elif dict1[key1]< dict3[key3]:
                d3c +=1
            else:
                continue

    for key3 in dict3:
        for key2 in dict2:
            if dict3[key3]> dict2[key2]:
                d3c +=1
            elif dict3[key3]< dict2[key2]:
                d2c +=1
            else:
                continue

    if (d1c>d2c and d1c>d3c):
        print("\ndict1 is greater")
    elif(d2c>d1c and d2c>d3c):
        print("\ndict2 is greater")
    else:
        print("\ndict3 is greater")


"""Function to add new elements in the dictionary"""
def addElm(dict1,dict2):
    print("\nb)Adding new elements to dict1 and dict2: ")
    newV1 = dict(j= 'Grapes')
    newV2 = dict(k= 'Pune')
    dict1.update(newV1)
    dict2.update(newV2)
    print("\ndict1: ",dict1)
    print("\ndict2: ",dict2)

"""Function to find the length of dict1 dict2 dict3"""
def length(dict1,dict2,dict3):
    print("\nc)Length of the dictionaries are: ")
    l1 = len(dict1)
    l2 = len(dict2)
    l3 = len(dict3)
    print("\nLength of dict1: ",l1)
    print("\nLength of dict2: ",l2)
    print("\nLength of dict3: ",l3)

"""Function to convert the dictionaries to strings and concatenate"""
def dictTOstr(dict1,dict2,dict3):
    print("\nd)Converting dictionaries to string and concatenating them:")
    dict1s = str(dict1)
    dict2s = str(dict2)
    dict3s = str(dict3)
    dicts = dict1s + dict2s + dict3s
    print("\nDictionaries as concatenated strings:\n",dicts)




"""Creating 3 dicionaries"""
dict1 = {'a':"Apples",'b':"Mango",'c':"Banana"}
dict2 = {'d':"Kolkata",'e':"Bangalore",'f':"Hyderabad"}
dict3 = {'g':"Suzuki",'h':"Honda",'i':"Yamaha"}

print("The 3 dictionaries given have the following values")
print("dict1: ",dict1,"\ndict2: ",dict2,"\ndict3: ",dict3)

"""Calling the Function"""
"""a) Comparing dictionaries to determine the biggest."""
compare(dict1,dict2,dict3)

"""b) Adding new elements in to the dictionaries dict1, dict2"""
addElm(dict1,dict2)


"""c) Printing the length of dict1, dict2, dict3."""
length(dict1,dict2,dict3)


"""d) Converting dict1, dict2, and dict3 dictionaries as string and concatenating all strings together."""
dictTOstr(dict1,dict2,dict3)



# Output:
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program37.py
# The 3 dictionaries given have the following values
# dict1:  {'a': 'Apples', 'b': 'Mango', 'c': 'Banana'}
# dict2:  {'d': 'Kolkata', 'e': 'Bangalore', 'f': 'Hyderabad'}
# dict3:  {'g': 'Suzuki', 'h': 'Honda', 'i': 'Yamaha'}
#
# a)Result after comparison:
#
# dict3 is greater
#
# b)Adding new elements to dict1 and dict2:
#
# dict1:  {'a': 'Apples', 'b': 'Mango', 'c': 'Banana', 'j': 'Grapes'}
#
# dict2:  {'d': 'Kolkata', 'e': 'Bangalore', 'f': 'Hyderabad', 'h': 'Pune'}
#
# c)Length of the dictionaries are:
#
# Length of dict1:  4
#
# Length of dict2:  4
#
# Length of dict3:  3
#
# d)Converting dictionaries to string and concatenating them:
#
# Dictionaries as concatenated strings:
#  {'a': 'Apples', 'b': 'Mango', 'c': 'Banana', 'j': 'Grapes'}{'d': 'Kolkata', 'e': 'Bangalore', 'f': 'Hyderabad', 'h': 'Pune'}{'g': 'Suzuki', 'h': 'Honda', 'i': 'Yamaha'}
#
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
