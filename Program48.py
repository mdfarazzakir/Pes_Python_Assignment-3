"""
Functions	Create a Calculator with the following functions.
a) Addition/subtraction/multiplication and division of two numbers (Note: Create separate function for 
each operation)
b) Find square root of a given number. (Use keyword arguments in your function)
c) Create a list of sub strings from a given string, such that sub strings are created with given character.
 i.e. String = "Pack: My: Box: With: Good: Food"
Create sub strings with the delimiter character ":" such that the following sub strings are created.
 substrlist=[Pack, My, Box, With, Good, Food] Note : Function should take at least 2 parameters
  ( Main string and delimiter character) return value from function will be list of substring.
"""


"""Importing math library"""
import math as m

"""a) Doing simple operations of Add, Sub, Multiply, Divide of two number using lambda function"""
"""Using try and except block for error handling"""
try:
    print("a) Calculator\n ")
    while True:
        option = int(input("Choose your option:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit\nOption: "))
        print("\n")
        if option == 0 or option > 5:
            print("Incorrect option\n")
        elif option == 5:
            print("Exiting the Calculator.\n")
            break
        else:
            FirstNum = eval(input("Enter the first number: "))
            print("\n")
            SecondNum = eval(input("Enter the second number: "))

            if option==1:
                add = lambda SecondNum:FirstNum+SecondNum
                FirstNum = add(SecondNum)
            elif option==2:
                subtract = lambda SecondNum:FirstNum-SecondNum
                FirstNum = subtract(SecondNum)
            elif option==3:
                multiply = lambda SecondNum:FirstNum*SecondNum
                FirstNum = multiply(SecondNum)
            elif option==4:
                divide = lambda SecondNum:FirstNum/SecondNum
                FirstNum = divide(SecondNum) 
            
            print("\n%d is the output"%FirstNum)
            print("\n")
           

    """b)Finding square root of a given number. (Use keyword arguments in your function)"""
    print("b) Square root operation: ")

    """**kwargs or keyword arguments means that the parameters to be passed in the function will be of type
    dictionary"""
       
    def squareRoot(**kwargs):
        for key in kwargs:
            return m.sqrt(kwargs[key])

    numForsqrt = eval(input("Enter the number which needs to be square rooted: "))

    res = (squareRoot(number = numForsqrt))
    print("The square root of %d is %.2f\n"%(numForsqrt,res))


    """c)Create a list of sub strings from a given string, such that sub strings are created with given character."""
    def subStrg(string,delimiterCharacter):
        return string.split(delimiterChr,6)


    strng = "Pack: My: Box: With: Good: Food"
    delimiterChr = ":"

    print("Original string :",strng)

    print("The list of sub string is ",subStrg(strng,delimiterChr))

   


except Exception as err:
    print("Error encountered, wrong input or check your code for error and execute again.")
    print("The error is: ",err)


# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>python Program48.py
# a) Calculator

# Choose your option:
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# 5.Exit
# Option: 1


# Enter the first number: 64


# Enter the second number: 198

# 262 is the output


# Choose your option:
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# 5.Exit
# Option: 2


# Enter the first number: 648


# Enter the second number: 657

# -9 is the output


# Choose your option:
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# 5.Exit
# Option: 3


# Enter the first number: 36  


# Enter the second number: 25

# 900 is the output


# Choose your option:
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# 5.Exit
# Option: 4


# Enter the first number: 36


# Enter the second number: 16

# 2 is the output


# Choose your option:
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# 5.Exit
# Option: 54


# Incorrect option

# Choose your option:
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# 5.Exit
# Option: 5


# Exiting the Calculator.

# b) Square root operation:
# Enter the number which needs to be square rooted: 15642
# The square root of 15642 is 125.07

# Original string : Pack: My: Box: With: Good: Food
# The list of sub string is  ['Pack', ' My', ' Box', ' With', ' Good', ' Food']

# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>