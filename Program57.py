"""
Exception Handling	Try implementing atleast any 5 exceptions in you program.
"""

"""Function to show Keyboard Interrupt"""
def KeyboardInterruptExm():
    try:
        while True:
            print("Loop running")
    except KeyboardInterrupt:
        print("Keyboard Interrupt\n")


"""Function to show ArithmeticError"""
def ArithmeticErrorExm():
    try:
        print("\nDivision of two numbers\n")
        num1 = eval(input("Enter num1: "))
        num2 = eval(input("Enter num2: "))
        product = num1 / num2
    except ArithmeticError as aErr:
        print("\nArithmeticError, provide correct data.")
        print("\nError is: ",aErr)
    else:
        print("\nDivision successful\n")
        print("\nThe result is ",product)

"""Function to show AssertionError"""
def AssertionErrorExm(pound):
    print("\nConverting non negative weight as pounds to kgs")
    try:
        assert(pound>=0),"Cannot accept negative weight"
        print("\nThe weight in kg is: ",pound*0.453592)
    except AssertionError as AErr:
        print("\nYour weight is of negative value.")
        print("\nError is ",AErr)



"""Function to show IOError while trying to write contents into the file that is opened in read mode only."""
def IOErrorExm(file):
    try:
        fopen = open(file,mode='r')
        print("\nData in the file: ",fopen.read())
        print("\na)Attempting write() operation.")
        fopen.write('Hello')
    except IOError as ioerr:
        print("\nYou cannot write data to a file which is in read mode.")
        print("\nError says ",ioerr)

"""Function to show ValueError"""
def ValueErrorExm():
    try:
        print("\nb)Attempting user input")
        data = int(input("Enter the data: "))
    except ValueError as verr:
        print("\nError, user input takes integer input, but a non integer input was given")
        print("\nError says ",verr)


print("1)Keyboard Interrupt")
KeyboardInterruptExm()

print("\n2)Arithmetic Error")
ArithmeticErrorExm()

print("\n3)Assertion Error")
AssertionErrorExm(7)
AssertionErrorExm(-5654)

print("\n4)IO Error")
file  = 'Program56Data.txt'
IOErrorExm(file)

print("\n5)Value Error")
ValueErrorExm()

# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>python Program57.py
# 1)Keyboard Interrupt
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


# 2)Arithmetic Error

# Division of two numbers

# Enter num1: 79
# Enter num2: 0

# ArithmeticError, provide correct data.

# Error is:  division by zero

# 3)Assertion Error

# Converting non negative weight as pounds to kgs

# The weight in kg is:  3.175144

# Converting non negative weight as pounds to kgs

# Your weight is of negative value.

# Error is  Cannot accept negative weight

# 4)IO Error

# Data in the file:  The soul is a Treasure chest; hidden inside of it are priceless jewels
# True wisdom is like an ocean; the deeper you go the greater the Treasure you'll find
# Trials are Treasure inside out
# Days are worth silver Months are worth gold Years are worth diamonds Eternity is priceless Treasure
# Truth is the heart's Treasure
# Children are the world's Treasure
# A genuine smile is one of the worldâ€™s rarest Treasure
# Your mind is gold Your heart is pearls Your soul is diamonds, Treasure is means your pricelesslife
# Treasure is where the world hides its wisdom
# Your mind is your wealth Your heart is your riches Your soul is your Treasure Your life is your reward

# a)Attempting write() operation.

# You cannot write data to a file which is in read mode.

# Error says  not writable

# 5)Value Error

# b)Attempting user input
# Enter the data: lk;hnvb

# Error, user input takes integer input, but a non integer input was given

# Error says  invalid literal for int() with base 10: 'lk;hnvb'

# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>