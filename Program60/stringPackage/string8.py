"""
Strings:
Apply all built in functions on Strings in your program. Note: There are 40 string functions. Use Tutorial for the help.
Note: Each program should have 5 string built in functions(so write 8 programs to cover all string functions)

"""

def strgOp():
    strg = input("Enter the string: ")
    print("\nYour enetered string is: ",strg)

    print("\nString operation using find return the lowest index in S where substring sub is found.: ")
    s = input("Enter the the character you want to find in the string: ")
    print("\nAfter performing find, string found at position: ",strg.find(s))

    print("\nString operation using format_map Return a formatted version of S, using substitutions from mapping.: ")
    a = {'x':'Russia', 'y':'Country','z':'World'}
    print("Using this dictionary for the following operation: ",a)
    print("\n{x} is the largest {y} in the {z}: ".format_map(a))

    print("\nString operation using format return a formatted version of S, using substitutions from args and kwargs.: ")
    print("\nAfter performing format(): ")
    print("{} is a fruit".format(strg))

    print("\nString operation using isupper Return True if the string is an uppercase string, False otherwise: ")
    print("After performing isupper: ")
    print(strg.isupper())

    print("\nString operation using islower return True if the string is a lowercase string, False otherwise: ")
    print("After performing islower: ")
    print(strg.islower())


strgOp()


# Output:
#
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program29_2.py
# Enter the string: Tomato
#
# Your enetered string is:  Tomato
#
# String operation using find return the lowest index in S where substring sub is found.:
# Enter the the character you want to find in the string: m
#
# After performing find, string found at position:  2
#
# String operation using format_map Return a formatted version of S, using substitutions from mapping.:
# Using this dictionary for the following operation:  {'x': 'Russia', 'y': 'Country', 'z': 'World'}
#
# Russia is the largest Country in the World:
#
# String operation using format return a formatted version of S, using substitutions from args and kwargs.:
#
# After performing format():
# Tomato is a fruit
#
# String operation using isupper Return True if the string is an uppercase string, False otherwise:
# After performing isupper:
# False
#
# String operation using islower return True if the string is a lowercase string, False otherwise:
# After performing islower:
# False
#
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
