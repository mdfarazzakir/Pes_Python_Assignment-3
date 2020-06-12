"""
Functions
Write a program with lambda function to perform following.
a) Perform all the operations of basic calculator (Add, Sub, Multiply, Divide, Modulus, Floor division)
"""

"""Doing simple operations of Add, Sub, Multiply, Divide, Modulus, Floor division using lambda function"""
try:
    while True:
        option = int(input("Choose your option:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Modulus\n6.Floor Division\n7.Exit\nOption: "))
        print("\n")
        if option == 0 or option > 7:
            print("Incorrect option")
        elif option == 7:
            print("Exiting the program.")
            break
        else:
            FirstNum = int(input("Enter the first number: "))
            print("\n")
            SecondNum = int(input("Enter the second number: "))

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
            elif option==5:
                modulus = lambda SecondNum:FirstNum%SecondNum
                FirstNum = modulus(SecondNum)
            elif option==6:
                floorDiv = lambda SecondNum:FirstNum//SecondNum
                FirstNum = floorDiv(SecondNum) 
            
            print("\n%d is the output"%FirstNum)
            print("\n")
           
except:
    print("Error encountered, wrong input or check your code for error and execute again.")

# Output:
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program44.py 
# Choose your option:
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# 5.Modulus
# 6.Floor Division
# 7.Exit
# Option: ,lknf
# Error encountered, wrong input or check your code for error and execute again.
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program44.py 
# Choose your option:
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# 5.Modulus
# 6.Floor Division
# 7.Exit
# Option: 1


# Enter the first number: 7


# Enter the second number: 9

# 16 is the output


# Choose your option:
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# 5.Modulus
# 6.Floor Division
# 7.Exit
# Option: 2


# Enter the first number: 54


# Enter the second number: 36

# 18 is the output


# Choose your option:
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# 5.Modulus
# 6.Floor Division
# 7.Exit
# Option: 3


# Enter the first number: 65 


# Enter the second number: 56

# 3640 is the output


# Choose your option:
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# 5.Modulus
# 6.Floor Division
# 7.Exit
# Option: 4


# Enter the first number: 634


# Enter the second number: 26

# 24 is the output


# Choose your option:
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# 5.Modulus
# 6.Floor Division
# 7.Exit
# Option: 5


# Enter the first number: 67


# Enter the second number: 35

# 32 is the output


# Choose your option:
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# 5.Modulus
# 6.Floor Division
# 7.Exit
# Option: 6


# Enter the first number: 89


# Enter the second number: 2

# 44 is the output


# Choose your option:
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# 5.Modulus
# 6.Floor Division
# 7.Exit
# Option: 7


# Exiting the program.
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ 