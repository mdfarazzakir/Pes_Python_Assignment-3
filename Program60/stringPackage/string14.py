def strgOp():
    strg = input("Enter the string: ")
    print("\nYour enetered string is: ",strg)

    print("\nString operation using title return a version of the string where each word is titlecased: ")
    print("\nAfter performing title:",strg.title())

    print("\nString operation using encode Encodes the string using the codec registered for encoding: ")
    print("\nAfter performing encode: ",strg.encode())

    print("\nString operation using isprintable return True if the string is printable, False otherwise: ")
    print("\nAfter performing isprintable: ",strg.isprintable())

    print("\nString operation using isspace return True if the string is a whitespace string, False otherwise: ")
    print("\nAfter performing isspace: ",strg.isspace())

    print("\nString operation using partition Partition the string into three parts using the given separator: ")
    pterm = input("\nEnter the partition character: ")
    print("\nAfter performing partition: ",strg.partition(pterm))


strgOp()

# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program29_8.py
# Enter the string: Pacific
#
# Your enetered string is:  Pacific
#
# String operation using title return a version of the string where each word is titlecased:
#
# After performing title: Pacific
#
# String operation using encode Encodes the string using the codec registered for encoding:
#
# After performing encode:  b'Pacific'
#
# String operation using isprintable return True if the string is printable, False otherwise:
#
# After performing isprintable:  True
#
# String operation using isspace return True if the string is a whitespace string, False otherwise:
#
# After performing isspace:  False
#
# String operation using partition Partition the string into three parts using the given separator:
#
# Enter the partition character: c
#
# After performing partition:  ('Pa', 'c', 'ific')
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
