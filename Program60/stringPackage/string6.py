"""
Strings:
Write a program to check how many ovals present in the given string. That is, count the number of " a e i o u" in the given string and
print the numbers against each oval. Example:- "This is Python" Number of total ovals = 3, i = 2, o =1

"""
"""Function to calculate vowels in a string"""
def vowels(strg):
    a = e = i = o = u = 0

    for j in strg:
        if j =='a':
            a = a + 1
        elif j == 'e':
            e = e + 1
        elif j =='i' :
             i= i + 1
        elif j == 'o':
            o = o + 1
        elif j =='u' :
             u = u + 1

    print("\nCount of a is: ",a)
    print("\nCount of e is: ",e)
    print("\nCount of i is: ",i)
    print("\nCount of o is: ",o)
    print("\nCount of u is: ",u)

    total= a+e+i+o+u
    print("\nTotal Vowels in strg is",total)

"""Taking string as input"""
strg = input("Enter the string: ").lower()

"""Calling the function"""

vowels(strg)

# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program28.py
# Enter the string: aeiou
#
# Count of a is:  1
#
# Count of e is:  1
#
# Count of i is:  1
#
# Count of o is:  1
#
# Count of u is:  1
#
# Total Vowels in strg is 5
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program28.py
# Enter the string: AEIOU
#
# Count of a is:  1
#
# Count of e is:  1
#
# Count of i is:  1
#
# Count of o is:  1
#
# Count of u is:  1
#
# Total Vowels in strg is 5
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program28.py
# Enter the string: United States
#
# Count of a is:  1
#
# Count of e is:  2
#
# Count of i is:  1
#
# Count of o is:  0
#
# Count of u is:  1
#
# Total Vowels in strg is 5
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program28.py
# Enter the string: India
#
# Count of a is:  1
#
# Count of e is:  0
#
# Count of i is:  2
#
# Count of o is:  0
#
# Count of u is:  0
#
# Total Vowels in strg is 3
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
