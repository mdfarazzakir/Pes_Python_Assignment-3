"""
Functions
Write a program to check given string is Palindrome or not. (Use function Concepts and Required keyword,
Default parameter concepts) i.e Reverse the given string and check whether it is same as original string,
if so then it is palindrome. Example: String "malayalam" when reversed will be "malayalam"
hence palindrome.

"""
"""Function for checking if a given string is plaindrome or not."""
def strgPalindrome(strg):
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

"""Using try and excpet block for error handling"""
try:
    """Taking sting input"""
    strg = input("Enter the string: ").lower()


    """Calling the function"""
    strgPalindrome(strg)
except:
    print("Error encountered, give the correct input or check the code.")


# Output:
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program45.py 
# Enter the string: Malayalam
# Palindrome
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program45.py 
# Enter the string: Kerala
# Not a palindrome
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ 