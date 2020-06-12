"""
File I/O Operations:
Write a program to perform following file operations
a) Open the file in read mode and read all its contents on to STDOUT.
b) Open the file in write mode and enter 5 new lines of strings in to the new file.
c) Open file in Append mode and add 5 lines of text into it.
"""

"""a)Program to open file in read mode and read all its contents on to STDOUT"""

def fileRead(file):
    with open(file,mode='r') as fopen:
        print("Data in the file is:")
        print(fopen.read())
        fopen.close()



"""b)Program to open the file in write mode and enter 5 new lines of strings in to the new file."""

def fileWrite(file):
    numOflines = int(input("Enter the number of lines want to add: "))
    with open(file,mode='w') as fopen:
        for _ in range(numOflines):
            data = eval(input("Enter the data you want to write to the file, add '' quotes if data is string or charecter:"))
            fopen.write("%s\n"%data)
    with open(file,mode='r') as fopen:
        print("\nNew Data:\n",fopen.read())
        fopen.close()


"""c)Program to open file in Append mode and add 5 lines of text into it."""

def fileAppend(file):
    numOflines = int(input("Enter the number of lines want to add: "))
    with open(file,mode='a') as fopen:
        for _ in range(numOflines):
            data = eval(input("Enter the data you want to add to the file, add '' quotes if data is string or charecter:"))
            fopen.write("%s\n"%data)
    with open(file,mode='r') as fopen:
        print("\nAfter adding new data:\n",fopen.read())
        fopen.close()

"""Initializing the file to a variable"""
file = 'Program49Data.txt'

try:
    print("a)Printing all the data in the file 'Program49Data.txt':\n")
    fileRead(file)

    print("\nb)Writing new data in the new file 'Program49Data.txt':\n")
    fileWrite(file)

    print("\nc)Adding data in the file 'Program49Data.txt':\n")
    fileAppend(file)
except Exception as err:
    print("Error encountered, please give the correct input or check the code")
    print("The error type is: ",err)

# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>python Program49.py
# a)Printing all the data in the file 'Program49Data.txt':

# Data in the file is:
# This is a file for Program49.
# This is a text file.
# This file is being used in the Program49 for File I/O processes.

# b)Writing new data in the new file 'Program49Data.txt':

# Enter the number of lines want to add: 5              
# Enter the data you want to write to the file, add '' quotes if data is string or charecter:'These lines are written in write mode'
# Enter the data you want to write to the file, add '' quotes if data is string or charecter:'The previous data has been erased as the file has been created newly'
# Enter the data you want to write to the file, add '' quotes if data is string or charecter:'The quick brown fox'
# Enter the data you want to write to the file, add '' quotes if data is string or charecter:'jumps over'
# Enter the data you want to write to the file, add '' quotes if data is string or charecter:'the lazy dog'

# New Data:
#  These lines are written in write mode
# The previous data has been erased as the file has been created newly
# The quick brown fox
# jumps over
# the lazy dog


# c)Adding data in the file 'Program49Data.txt':

# Enter the number of lines want to add: 5
# Enter the data you want to add to the file, add '' quotes if data is string or charecter:'These below line are written in append mode'
# Enter the data you want to add to the file, add '' quotes if data is string or charecter:'New lines will be added below the lines that were written previously'
# Enter the data you want to add to the file, add '' quotes if data is string or charecter:'The sentence, The quick brown fox jumps over the lazy dog'
# Enter the data you want to add to the file, add '' quotes if data is string or charecter:',contains all the letters of the English Alphabet'
# Enter the data you want to add to the file, add '' quotes if data is string or charecter:'All 26 letter'

# After adding new data:
#  These lines are written in write mode
# The previous data has been erased as the file has been created newly
# The quick brown fox
# jumps over
# the lazy dog
# These below line are written in append mode
# New lines will be added below the lines that were written previously
# The sentence, The quick brown fox jumps over the lazy dog
# ,contains all the letters of the English Alphabet
# All 26 letter


# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>python Program49.py
# a)Printing all the data in the file 'Program49Data.txt':

# Data in the file is:
# These lines are written in write mode
# The previous data has been erased as the file has been created newly
# The quick brown fox
# jumps over
# the lazy dog
# These below line are written in append mode
# New lines will be added below the lines that were written previously
# The sentence, The quick brown fox jumps over the lazy dog
# ,contains all the letters of the English Alphabet
# All 26 letter


# b)Writing new data in the new file 'Program49Data.txt':

# Enter the number of lines want to add: jdw
# Error encountered, please give the correct input or check the code
# The error type is:  invalid literal for int() with base 10: 'jdw'

# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>