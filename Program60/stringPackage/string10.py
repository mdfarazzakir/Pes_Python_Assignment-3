def strgOp():
    strg = input("Enter the string: ")
    print("\nYour enetered string is: ",strg)

    print("\nString operation using index return the lowest index in S where substring sub is found: ")
    s = input("Enter the charecter from the string you want to locate the index of: ")
    print("\nAfter performing index:",strg.index(s))

    print("\nString operation using isnumeric return True if the string is a numeric string, False otherwise: ")
    print("\nAfter performing isnumeric: ",strg.isnumeric())

    print("\nString operation using istitle return True if the string is a title-cased string, False otherwise: ")
    print("\nAfter performing istitle: ",strg.istitle())

    print("\nString operation using ljust return a left-justified string of length width: ")
    print("\nAfter performing ljust: ",strg.ljust(50,s))

    print("\nString operation using rjust return a right-justified string of length width: ")
    print("\nAfter performing rjust: ",strg.rjust(50,s))

    print("\nString operation zfill Pad a numeric string with zeros on the left, to fill a field of the given width: ")
    print("\nAfter performing zfill: ",strg.zfill(20))

strgOp()


# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program29_4.py
# Enter the string: Bengaluru
#
# Your enetered string is:  Bengaluru
#
# String operation using index return the lowest index in S where substring sub is found:
# Enter the charecter from the string you want to locate the index of: a
#
# After performing index: 4
#
# String operation using isnumeric return True if the string is a numeric string, False otherwise:
#
# After performing isnumeric:  False
#
# String operation using istitle return True if the string is a title-cased string, False otherwise:
#
# After performing istitle:  True
#
# String operation using ljust return a left-justified string of length width:
#
# After performing ljust:  Bengaluruaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
#
# String operation using rjust return a right-justified string of length width:
#
# After performing rjust:  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaBengaluru
#
# String operation zfill Pad a numeric string with zeros on the left, to fill a field of the given width:
#
# After performing zfill:  00000000000Bengaluru
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
