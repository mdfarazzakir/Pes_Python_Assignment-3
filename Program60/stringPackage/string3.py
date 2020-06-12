"""
Strings:
Write a program to print the different data types (Numbers, strings characters) using the Format symbols (Refer to different format symbols specified in Tutorial)

"""
"""Function for String datatype"""
def stringType():
    val = eval(input("\nGive the input as string: "))
    print("Using modulus s to print the string as %s"%val)
    print("Printing the datatype: ",type(val))

def integerType():
    val = eval(input("\nGive the input as integer: "))
    print("Using modulus d to print the number as integer as %d"%val)
    print("Printing the datatype: ",type(val))

def charecterType():
    val = eval(input("\nGive the input as character: "))
    print("Using modulus c to print the number as character as %c"%val)
    print("Printing the datatype: ",type(val))

def floatType():
    val = eval(input("\nGive the input as float: "))
    print("Using modulus f to print the number as float as %f"%val)
    print("Using modulus .2f to print the number as float as %.2f"%val)
    print("Printing the datatype: ",type(val))

def complexType():
    real = eval(input("\nEnter the real part: "))
    img = eval(input("\nEnter the imaginary part: "))
    val = complex(real,img)
    print("Using \complex(real,img) to get the number as complex number as",val)
    print("Printing the datatype: ",type(val))


stringType()

integerType()

charecterType()

floatType()

complexType()

# Output:
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program25.py
#
# Give the input as string: 'Australia'
# Using modulus s to print the string as Australia
# Printing the datatype:  <class 'str'>
#
# Give the input as integer: 7456
# Using modulus d to print the number as integer as 7456
# Printing the datatype:  <class 'int'>
#
# Give the input as character: 'V'
# Using modulus c to print the number as character as V
# Printing the datatype:  <class 'str'>
#
# Give the input as float: 4257.1385
# Using modulus f to print the number as float as 4257.138500
# Using modulus .2f to print the number as float as 4257.14
# Printing the datatype:  <class 'float'>
#
# Enter the real part: 8
#
# Enter the imaginary part: 6
# Using \complex(real,img) to get the number as complex number as (8+6j)
# Printing the datatype:  <class 'complex'>
#
# C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
