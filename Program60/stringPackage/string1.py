"""
Basic String operations:

Write a program to read string and print each character separately.
    a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.
    b) Repeat the string 100 times using repeat operator *
    c) Read string 2 and concatenate with other string using + operator.

"""

"""Printing the string with character separately"""
def oneChar():
    print("Printing the string with character separately")
    strg = input("Enter the string:")
    for i in strg:
        print(i)

"""String slicing"""
def slice():
    print("\nString slicing")
    strg = input("Enter the string: ")

    l = len(strg) #Length of the string

    slice1 = strg[:l//2]
    slice2 = strg[l//2:]

    print("\n1) ",slice1," is the first half of the string\n2)",slice2," is the second half of the string")


"""String repeatition"""
def repeat():
    print("\nString repeatition")
    strg = input("Enter the string: ")
    print("Repeating ",strg)
    print("%s\n" %strg*100)


"""String concatenation"""
def concat():
    print("\nString concatenation")
    strg1 = input("Enter the string 2: ")

    strg2 = input("Enter another string to concatenate: ")

    print(strg1+strg2,end=" ")

"""Calling the fucntions"""
oneChar()

slice()

repeat()

concat()

# Output
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-1>python Program6.py
# Printing the string with character separately
# Enter the string:Bengaluru
# B
# e
# n
# g
# a
# l
# u
# r
# u
#
# String slicing
# Enter the string: Australia
#
# 1)  Aust  is the first half of the string
# 2) ralia  is the second half of the string
#
# String repeatition
# Enter the string: Egg
# Repeating  Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
# Egg
#
#
# String concatenation
# Enter the string 2: 2
# Enter another string to concatenate: Apples
# 2Apples
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-1>
