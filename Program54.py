"""
Exception Handling	Write a program to handle the following exceptions in you program.
a) KeyboardInterrupt
b) NameError 
c) ArithmeticError Note: Make use of try, except, else: block statements.
"""
"""a) Keyboard Interrupt"""
"""Using try and except block to catch the error"""
try:
    while True:
        print("Loop running")
except KeyboardInterrupt as err:
    print("Keyboard Interrupt\n")

"""b) NameError"""
"""Using try and except block to catch the error"""
try:
    data = input("Enter the value for data: ")
    print(datas)
except NameError as nerr:
    print("Name Error\n",nerr,"\n")

"""c) ArithmeticError"""
"""Using try and except block to catch the error"""
try:
    print("Division of two numbers\n")
    num1 = eval(input("Enter num1: "))
    num2 = eval(input("Enter num2: "))
    product = num1 / num2
except ArithmeticError as aErr:
    print("ArithmeticError, provide correct data.")
    print("Error is: ",aErr)
else:
    print("Division successful\n")
    print("The result is ",product)


# Output:
# Scenario 1:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>python Program54.py
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Keyboard Interrupt

# Enter the value for data: 9
# Name Error
#  name 'datas' is not defined

# Division of two numbers

# Enter num1: 7
# Enter num2: 6
# Division successful

# The result is  1.1666666666666667

# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>


# Scenario 2:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>python Program54.py
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Loop running
# Keyboard Interrupt

# Enter the value for data: 5
# Name Error
#  name 'datas' is not defined

# Division of two numbers

# Enter num1: 646
# Enter num2: 0
# ArithmeticError, provide correct data.
# Error is:  division by zero

# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>