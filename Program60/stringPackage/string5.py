"""
Strings:
Write a program to check given string is Palindrome or not.That is reverse the given string and check whether it is same as original string, if so
then it is palindrome.Example: String = "malayalam"  reverse string = "malayalam" hence given string is palindrome. Use built functions to check
given string is palindrome or not.

"""

"""Taking sting input"""
strg = input("Enter the string: ")

"""Length of the string"""
sL = len(strg)

"""Intializing a variable as string"""
strg1 = str()

for i in range(sL-1,-1,-1):
    strg1 = strg1 + strg[i]

if strg1 ==strg:
    print("Palindrome")
else:
    print("Not a palindrome")

# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program27.py
# Enter the string: Arora
# Not a palindrome
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program27.py
# Enter the string: malayalam
# Palindrome
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program27.py
# Enter the string: arora
# Palindrome
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program27.py
# Enter the string: aaaabbbaaa
# Not a palindrome
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program27.py
# Enter the string: aaabbbaaa
# Palindrome
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program27.py
# Enter the string: acacacaca
# Palindrome
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program27.py
# Enter the string: acacacacac
# Not a palindrome
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program27.py
# Enter the string: acacacaa
# Not a palindrome
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>ccaaccaacc
# 'ccaaccaacc' is not recognized as an internal or external command,
# operable program or batch file.
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program27.py
# Enter the string: ccaaccaaccaacc
# Palindrome
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
