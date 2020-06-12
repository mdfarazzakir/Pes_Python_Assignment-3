def strgOp():
    strg = input("Enter the string: ")
    print("\nYour enetered string is: ",strg)

    print("\nString operation using splitlines return a list of the lines in the string, breaking at line boundaries: ")
    print("\nAfter performing splitlines:",strg.splitlines())

    print("\nString operation using split returns a list of the words in the string, using sep as the delimiter string: ")
    print("\nAfter performing split: ",strg.split())

    print("\nString operation using rsplit return a list of the words in the string, using sep as the delimiter string: ")
    print("\nAfter performing rsplit: ",strg.rsplit())

    print("\nString operation using rindex returns the highest index in S where substring sub is found: ")
    stg =input("Enter the term for index: ")
    print("\nAfter performing rindex: ",strg.rindex(stg))

    print("\nString operation using swapcase Convert uppercase characters to lowercase and lowercase characters to uppercas: ")
    sterm = input("\nEnter the string: ")
    print("\nAfter performing swapcase: ",sterm.swapcase())


strgOp()

# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program29_7.py
# Enter the string: United Kingdom
#
# Your enetered string is:  United Kingdom
#
# String operation using splitlines return a list of the lines in the string, breaking at line boundaries:
#
# After performing splitlines: ['United Kingdom']
#
# String operation using split returns a list of the words in the string, using sep as the delimiter string:
#
# After performing split:  ['United', 'Kingdom']
#
# String operation using rsplit return a list of the words in the string, using sep as the delimiter string:
#
# After performing rsplit:  ['United', 'Kingdom']
#
# String operation using rindex returns the highest index in S where substring sub is found:
# Enter the term for index: g
#
# After performing rindex:  10
#
# String operation using swapcase Convert uppercase characters to lowercase and lowercase characters to uppercas:
#
# Enter the string: UnItEd KiNgDoM
#
# After performing swapcase:  uNiTeD kInGdOm
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
