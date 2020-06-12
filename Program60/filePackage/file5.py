"""
File I/O Operations:
Open the file in read & write mode and apply following functions
a) All 13 functions mentioned in Tutorial File object table.
"""

"""Using all the mentioned 13 functions"""

"""Assigning file to a varable"""
file = 'Program53Data.txt'


"""Using try and except block for exception handling"""
try:
    """Opening a file in read mode"""
    fopen = open(file,mode='r')
    print("1)To check if the file is opened we will try to print the file:")
    print("Output is:")
    for i in fopen:
        print(i)
    """1) Function to close the file: close()"""
    fopen.close()
    print("\nAfter closing the file we should not be able to open the file:\n")
    print("Output is:")
    for i in fopen:
        print(i)

except Exception as err:
    print("Error encountered")
    print(err)
    print("You are getting this error because the file is closed")

"""Opening a file in read and write(r+) mode"""
fopen = open(file,mode='r+')

"""2)Using the function filno(), returns an integer number (file descriptor) of the file."""
print("\n2)The function fileno() returns an integer number (file descriptor) of the file.")
print("Output is:",fopen.fileno())

"""3)Using the function isatty(), returns True if the file stream is interactive."""
print("\n3)The function isatty(), returns True if the file stream is interactive.")
print("Output is:",fopen.isatty())


"""4)Using the function read(n), reads at most n characters from the file.
Reads till end of file if it is negative or None"""
print("\n4)The function read(n),reads at most n characters from the file.")
print("Output is:",fopen.read(30))

"""5)Using function readable(), returns True if the file stream can be read from."""
print("\n5)The function readable(),returns True if the file stream can be read from.")
print("Output is:",fopen.readable())

"""6)Using function readline(),reads and returns one line from the file. Reads in at most n bytes if specified."""
print("\n6)The function readline()reads and returns one line from the file. Reads in at most n bytes if specified.")
print("Output is:",fopen.readline())

"""7)Using the function readlines(),reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified."""
print("\n7)The function readlines(),reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.")
print("Output is:",fopen.readlines())
fopen.close()

"""Opening the file in read and write mode"""
fopen = open(file,mode='r+')
"""8)Using the function seek(),changes the file position to offset bytes, in reference to from (start, current, end)."""
print("\n8)Using the function seek(),changes the file position to offset bytes, in reference to from (start, current, end).")
print("Output is:",fopen.seek(0,2))

"""9)Using the function seekable(), returns True if the file stream supports random access."""
print("\n9)The function seekable(), returns True if the file stream supports random access.")
print("Output is:",fopen.seekable())

"""10)Using the function tell(), returns the current file location."""
print("\n10)The function tell(), returns the current file location.")
print("Output is:",fopen.tell())

"""11)Using the function writable(),returns True if the file stream can be written to."""
print("\n11)The function writable(),returns True if the file stream can be written to.")
print("Output is:",fopen.writable())

"""12)The function write(), writes the string s to the file and returns the number of characters written."""
print("\n12)The function write(), writes the string s to the file and returns the number of characters written.")
charactersWritten = fopen.write('\nBengalure is in South India')
print("Output is:",charactersWritten,"characters written")


"""13)The function writelines(), Writes a list of lines to the file."""
print("\n13)The function writelines(), Writes a list of lines to the file.")
fopen.writelines(["\n","The quick brown fox jumps over the lazy dog","Life is either a daring adventure or nothing at all","You will face many defeats in life, but never let yourself be defeated"])
print("Output is:")
for i in open(file).readlines():
    print(i)

print("Last 2 lines are newly added lines")


# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>python Program53.py
# 1)To check if the file is opened we will try to print the file:
# Output is:
# Amidst the worldâ€™s trash is sometimes where you will find Godâ€™s Treasure

# Knowledge is a unique Treasure which no one can acquire easily

# Where the world hides wisdom the universe places its Treasure

# True wisdom is like an ocean the deeper you the greater the Treasure you'll find

# Children are our greatest Treasure

# If gold was as plentiful as sand, it would not be as valuable as Treasure

# Riches you hold in your hands are inferior to Treasure you store in your heart

# Riches you hold in your hands are inferior to Treasure you harbor in your heart

# Wealth is a small blessing, health is a great asset, happiness is an extraordinary Treasure and life is a remarkable reward

# When you Treasure what you have, you are already rich

# After closing the file we should not be able to open the file:

# Output is:
# Error encountered
# I/O operation on closed file.
# You are getting this error because the file is closed

# 2)The function fileno() returns an integer number (file descriptor) of the file.
# Output is: 3

# 3)The function isatty(), returns True if the file stream is interactive.
# Output is: False

# 4)The function read(n),reads at most n characters from the file.
# Output is: Amidst the worldâ€™s trash is

# 5)The function readable(),returns True if the file stream can be read from.
# Output is: True

# 6)The function readline()reads and returns one line from the file. Reads in at most n bytes if specified.
# Output is: sometimes where you will find Godâ€™s Treasure


# 7)The function readlines(),reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
# Output is: ['Knowledge is a unique Treasure which no one can acquire easily\n', 'Where the world hides wisdom the universe places its Treasure\n', "True wisdom is like an ocean the deeper you the greater the Treasure you'll find\n", 'Children are our greatest Treasure\n', 'If gold was as plentiful as 
# sand, it would not be as valuable as Treasure\n', 'Riches you hold in your hands are inferior to Treasure you store in your heart\n', 'Riches you hold 
# in your hands are inferior to Treasure you harbor in your heart\n', 'Wealth is a small blessing, health is a great asset, happiness is an extraordinary Treasure and life is a remarkable reward\n', 'When you Treasure what you have, you are already rich']

# 8)Using the function seek(),changes the file position to offset bytes, in reference to from (start, current, end).
# Output is: 737

# 9)The function seekable(), returns True if the file stream supports random access.
# Output is: True

# 10)The function tell(), returns the current file location.
# Output is: 737

# 11)The function writable(),returns True if the file stream can be written to.
# Output is: True

# 12)The function write(), writes the string s to the file and returns the number of characters written.
# Output is: 28 characters written

# 13)The function writelines(), Writes a list of lines to the file.
# Output is:
# Amidst the worldâ€™s trash is sometimes where you will find Godâ€™s Treasure

# Knowledge is a unique Treasure which no one can acquire easily

# Where the world hides wisdom the universe places its Treasure

# True wisdom is like an ocean the deeper you the greater the Treasure you'll find

# Children are our greatest Treasure

# If gold was as plentiful as sand, it would not be as valuable as Treasure

# Riches you hold in your hands are inferior to Treasure you store in your heart

# Riches you hold in your hands are inferior to Treasure you harbor in your heart

# Wealth is a small blessing, health is a great asset, happiness is an extraordinary Treasure and life is a remarkable reward

# When you Treasure what you have, you are already rich
# Last 2 lines are newly added lines

# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>