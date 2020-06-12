"""
File I/O Operations:
In a given directory search all text files for the pattern "Treasure". 
a) Find how many text files has the pattern.
b) Count how many times pattern repeats in each file Note: Create at least 4 text files in a directory
and keep the pattern in at least 2 files.
 Repeat the pattern in the file many times.
"""

"""Importing glob library so that we can read all the files a specific location at one time"""
import glob
totalcount = 0

"""a) Finding how many text files has the pattern 'Treasure'."""
print("a)Printing the text files having the mentioned pattern.")
"""Reading the file through glob method"""
for file in glob.glob('Program51Folder/*.txt'):
    f  = open(file,mode='r')

    fopen = f.read().split()
    if 'Treasure' in fopen:
        totalcount = fopen.count('Treasure')
        print("\nFile ",file,"has total 'Treasure' word count of ",totalcount)
        totalcount += fopen.count('Treasure')
    else:
        print("\nFile ",file,"has 'Treasure' word count of",0)


"""b)Count how many times pattern repeats in each file Note: Create at least 4 text files in a directory
and keep the pattern in at least 2 files."""
    
print("\nb)Total 'Treasure' word count adding all the files is ",totalcount)


# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>python Program51.py
# a)Printing the text files having the mentioned pattern.

# File  Program51Folder\Program51Data1.txt has total 'Treasure' word count of  10

# File  Program51Folder\Program51Data2.txt has total 'Treasure' word count of  10

# File  Program51Folder\Program51Data3.txt has 'Treasure' word count of 0        

# File  Program51Folder\Program51Data4.txt has 'Treasure' word count of 0        

# b)Total 'Treasure' word count adding all the files is  20

# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>