def strgOp():
    strg = input("Enter the string: ")
    print("\nYour enetered string is: ",strg)

    print("\nString operation using startswith return True if S starts with the specified prefix, False otherwise: ")
    stg1 = input("Enter the string for check: ")
    print("\nAfter performing startswith:",strg.startswith(stg1))

    print("\nString operation using endswith return True if S ends with the specified suffix, False otherwise: ")
    stg2 = input("Enter the string for check: ")
    print("\nAfter performing endswith: ",strg.endswith(stg2))

    print("\nString operation using join Concatenate any number of strings: ")
    print("\nJoining the strings from whitspace position: ",strg.join(" "))

    print("\nString operation using rfind return the highest index in S where substring sub is found: ")
    stg3 = input("Enter the string to find its position: ")
    print("\nAfter performing rfind: ",strg.rfind(stg3))

    print("\nString operation using strip return a copy of the string with leading and trailing whitespace remove: ")
    print("\nAfter performing strip: ",strg.strip())


strgOp()


# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program29_6.py
# Enter the string: Anaconda
#
# Your enetered string is:  Anaconda
#
# String operation using startswith return True if S starts with the specified prefix, False otherwise:
# Enter the string for check: A
#
# After performing startswith: True
#
# String operation using endswith return True if S ends with the specified suffix, False otherwise:
# Enter the string for check: a
#
# After performing endswith:  True
#
# String operation using join Concatenate any number of strings:
#
# Joining the strings from whitspace position:
#
# String operation using rfind return the highest index in S where substring sub is found:
# Enter the string to find its position: a
#
# After performing rfind:  7
#
# String operation using strip return a copy of the string with leading and trailing whitespace remove:
#
# After performing strip:  Anaconda
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
