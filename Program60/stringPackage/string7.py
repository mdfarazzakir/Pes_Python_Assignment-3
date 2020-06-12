"""
Strings:
Apply all built in functions on Strings in your program. Note: There are 40 string functions. Use Tutorial for the help.
Note: Each program should have 5 string built in functions(so write 8 programs to cover all string functions)

"""

def strgOp():
    strg = input("Enter the string: ")
    print("\nYour enetered string is: ",strg)

    print("\nString operation using capitalize returns a capitalized version of the string.: ")
    print("\nAfter performing capitalize: ",strg.capitalize())

    print("\nString operation using casefold returns a version of the string suitable for caseless comparisons.: ")
    print("\nAfter performing casefold: ",strg.casefold())

    print("\nString operationusing center returns a centered string of length width.: ")
    print("\nAfter performing centre: ",strg.center(50))

    print("\nString operation using count returns the number of non-overlapping occurrences of substring sub in: ")
    sc = input("\nEnter the string you want to count:")
    print("\nTotal count is: ",strg.count(sc))

    print("\nString operation using expandtabs returns a copy where all tab characters are expanded using spaces.: ")
    strg1 = "Tab \tcharecter"
    print("Using string input as 'Tab \\tcharecter'")
    print("\nAfter performing expandtabs: ",strg1.expandtabs())

    print("\nString operation using isidentifier returns True if the string is a valid Python identifier, False otherwise.: ")
    print("\nAfter performing isidentifier: ",strg.isidentifier())

strgOp()


# Output:
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program29_1.py
# Enter the string: Hello world
#
# Your enetered string is:  Hello world
#
# String operation using capitalize returns a capitalized version of the string.:
#
# After performing capitalize:  Hello world
#
# String operation using casefold returns a version of the string suitable for caseless comparisons.:
#
# After performing casefold:  hello world
#
# String operationusing center returns a centered string of length width.:
#
# After performing centre:                     Hello world
#
# String operation using count returns the number of non-overlapping occurrences of substring sub in:
#
# Enter the string you want to count:w
#
# Total count is:  1
#
# String operation using expandtabs returns a copy where all tab characters are expanded using spaces.:
# Using string input as 'Tab \tcharecter'
#
# After performing expandtabs:  Tab     charecter
#
# String operation using isidentifier returns True if the string is a valid Python identifier, False otherwise.:
#
# After performing isidentifier:  False
#
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
