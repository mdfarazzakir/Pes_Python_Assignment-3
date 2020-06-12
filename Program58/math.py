"""
Modules & Packages	Create file called  "calc.py" which has following functions
i) functions to add 2 numbers
ii) function to find diff of 2 numbers
iii) function to multiply 2 numbers
iv) all maths operations ( sqrt, div, floor div, modulus, primenumber)
v) Fibonacci series
        
a) Write a new program in file "maths.py" such that you import functions of file "calc.py" to your new program
b) Use From <module> import <function> statement to import only few function  from calc module.
"""
"""For all the different types of operation the functions have been imported exclusively from calc.py file"""

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
numForsqrt = int(input("Enter the number for square root operation: "))
numForprime = int(input("Enter the number for prime number operation: "))
numForfibo = int(input("Enter the number for fibonacci series operation: "))


"""i) Function to add 2 numbers"""
from calc import add
print("\ni)Functions to add %d and %d"%(num1,num2))
print("Output of adding two numbers: ",add(num1,num2))

"""ii) Function to find diff of 2 numbers"""
from calc import subtract
print("\nii) Function to find diff of %d and %d"%(num1,num2))
print("Output of subtracting two numbers: ",subtract(num1,num2))

"""iii) Function to multiply 2 numbers"""
from calc import multiply
print("\niii) Function to multiply %d and %d"%(num1,num2))
print("Output of multiplying two numbers: ",multiply(num1,num2))

"""iv) Function to do all maths operations ( sqrt, div, floor div, modulus, primenumber)"""
print("\niv) Function to do all maths operations ( sqrt, div, floor div, modulus, primenumber)")

from calc import squareRoot
print("\nFunction to find square root of %d"%numForsqrt)
print("Output of square rooting a number: ",squareRoot(numForsqrt))

from calc import divide
print("\nFunction to divide %d and %d"%(num1,num2))
print("Output of dividing two numbers: ",divide(num1,num2))

from calc import floorDiv
print("\nFunction to do floor division on %d and %d"%(num1,num2))
print("Output of floor division of two numbers: ",floorDiv(num1,num2))

from calc import modulus
print("\nFunction to divide %d and %d using modulus operator"%(num1,num2))
print("Output of modulus two numbers: ",modulus(num1,num2))

from calc import primeNumber
print("\nFunction to check if the number is prime or not")
primeNumber(numForprime)

"""v) Function to generate fibonacci series"""
from calc import fibo
print("\nv)Functions to generate fibonacci series")
print("Output: ")
fibo(numForfibo)


# Output:
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3\Program58>python math.py
# Enter num1: 14
# Enter num2: 9
# Enter the number for square root operation: 246
# Enter the number for prime number operation: 43
# Enter the number for fibonacci series operation: 11

# i)Functions to add 14 and 9
# Output of adding two numbers:  23    

# ii) Function to find diff of 14 and 9
# Output of subtracting two numbers:  5

# iii) Function to multiply 14 and 9
# Output of multiplying two numbers:  126

# iv) Function to do all maths operations ( sqrt, div, floor div, modulus, primenumber)

# Function to find square root of 246
# Output of square rooting a number:  15.684387141358123

# Function to divide 14 and 9
# Output of dividing two numbers:  1.5555555555555556

# Function to do floor division on 14 and 9
# Output of floor division of two numbers:  1

# Function to divide 14 and 9 using modulus operator
# Output of modulus two numbers:  5

# Function to check if the number is prime or not
# 43  is a prime number

# v)Functions to generate fibonacci series
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55

# C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3\Program58>