def strgOp():
    strg = input("Enter the string: ")
    print("\nYour enetered string is: ",strg)

    print("\nString operation using lstrip return  a copy of the string with leading whitespace removed: ")
    print("\nAfter performing lstrip:",strg.lstrip())

    print("\nString operation using rstrip return a copy of the string with trailing whitespace removed: ")
    print("\nAfter performing rstrip: ",strg.rstrip())

    print("\nString operation using lower return a copy of the string converted to lowercase: ")
    print("\nAfter performing lower: ",strg.lower())

    print("\nString operation using upper return a copy of the string converted to uppercase.: ")
    print("\nAfter performing upper: ",strg.upper())

    print("\nString operation using replace return a copy with all occurrences of substring old replaced by new: ")
    st1=input("Enter the string you want to add as a replacement: ")
    print("\nAfter performing replace: ",strg.replace(strg,st1))

    print("\nString operation rpartition Partition the string into three parts using the given separator: ")
    stg=input("Enter a string: ")
    print("\nGiven string: ",stg)
    pterm = input("\nEnter the partition character: ")
    print("\nAfter performing rpartition: ",stg.rpartition(pterm))

strgOp()

# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program29_5.py
# Enter the string: AmAzOn
#
# Your enetered string is:  AmAzOn
#
# String operation using lstrip return  a copy of the string with leading whitespace removed:
#
# After performing lstrip: AmAzOn
#
# String operation using rstrip return a copy of the string with trailing whitespace removed:
#
# After performing rstrip:  AmAzOn
#
# String operation using lower return a copy of the string converted to lowercase:
#
# After performing lower:  amazon
#
# String operation using upper return a copy of the string converted to uppercase.:
#
# After performing upper:  AMAZON
#
# String operation using replace return a copy with all occurrences of substring old replaced by new:
# Enter the string you want to add as a replacement: AmazoN
#
# After performing replace:  AmazoN
#
# String operation rpartition Partition the string into three parts using the given separator:
# Enter a string: Hello
#
# Given string:  Hello
#
# Enter the partition character: l
#
# After performing rpartition:  ('Hel', 'l', 'o')
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
