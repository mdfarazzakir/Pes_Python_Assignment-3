"""
Exception Handling:
Write a program to handle following exceptions using Try block.
a) IO Error while you try writing contents into the file that is opened in read mode only.
b) ValueError
"""

"""a)Showing IOError while trying to write contents into the file that is opened in read mode only."""
file  = 'Program56Data.txt'
fopen = open(file,mode='r')

try:
    print("\nData in the file: ",fopen.read())
    print("\na)Attempting write() operation.")
    fopen.write('Hello')
except IOError as ioerr:
    print("\nYou cannot write data to a file which is in read mode.")
    print("\nError says ",ioerr)

"""2)Showing ValueError"""
try:
    print("\nb)Attempting user input")
    data = int(input("Enter the data: "))
except ValueError as verr:
    print("\nError, user input takes integer input, but a non integer input was given")
    print("\nError says ",verr)

# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>python Program56.py

# Data in the file:  The soul is a Treasure chest; hidden inside of it are priceless jewels
# True wisdom is like an ocean; the deeper you go the greater the Treasure you'll find
# Trials are Treasure inside out
# Days are worth silver Months are worth gold Years are worth diamonds Eternity is priceless Treasure   
# Truth is the heart's Treasure
# Children are the world's Treasure
# A genuine smile is one of the worldâ€™s rarest Treasure
# Your mind is gold Your heart is pearls Your soul is diamonds, Treasure is means your pricelesslife    
# Treasure is where the world hides its wisdom
# Your mind is your wealth Your heart is your riches Your soul is your Treasure Your life is your reward

# a)Attempting write() operation.

# You cannot write data to a file which is in read mode.

# Error says  not writable

# b)Attempting user input
# Enter the data: kjgd

# Error, user input takes integer input, but a non integer input was given

# Error says  invalid literal for int() with base 10: 'kjgd'

# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>