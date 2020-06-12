"""
Functions
Write a function to find the biggest of 4 numbers.
a) All numbers are passed as arguments separately (Required argument)
b) use default values for arguments (Default arguments)
"""

"""Function to find the biggest of 4 numbers"""
"""The function itself has default values assigned to the arguments and overwrites if external
 values are given"""

def biggest(n1=1,n2=2,n3=3,n4=4):
    #Initializing n4 as the biggest value
    biggest = n4
    if n1>n2 and n1>n3 and n1>n4:
        biggest=n1
    elif n2>n1 and n2>n3 and n2>n4:
        biggest=n2
    elif n3>n1 and n3>n2 and n3>n4:
        biggest=n3
    else:
        biggest=n4
    print("\n%d is the biggest of %d %d %d and %d"%(biggest,n1,n2,n3,n4))


num1=num2=num3=num4=0

try:
    while True:
        option = int(input("\nChoose your option:\n1.Comparing with default values\n2.Provide with new values\n3.Exit\nOption: "))
        if option==0 or option>3:
            print("\nInvalid option.")
        elif option == 3:
            print("\nExiting the program.")
            break
        else:
            if option == 1:
                print("\nThe default values are 1,2,3,4")
                print("\nComparing among default values: ")
                biggest()
            elif option== 2:

                for i in (num1,num2,num3,num4):
                    if i == num1:
                        num1 =eval(input("Enter value for num1: "))
                    elif i == num2:
                        num2 =eval(input("Enter value for num2: "))
                    elif i == num3:
                        num3 =eval(input("Enter value for num3: "))
                    else:
                        num4 =eval(input("Enter value for num4: "))

                biggest(num1,num2,num3,num4)
            
except:
    print("\nError encountered, give the correct input or check the code")

# Output:
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program46.py 

# Choose your option:
# 1.Comparing with default values
# 2.Provide with new values
# 3.Exit
# Option: 1

# The default values are 1,2,3,4

# Comparing among default values: 

# 4 is the biggest of 1 2 3 and 4

# Choose your option:
# 1.Comparing with default values
# 2.Provide with new values
# 3.Exit
# Option: 2
# Enter value for num1: 45
# Enter value for num2: 24
# Enter value for num3: 684
# Enter value for num4: 3654

# 3654 is the biggest of 45 24 684 and 3654

# Choose your option:
# 1.Comparing with default values
# 2.Provide with new values
# 3.Exit
# Option: 3

# Exiting the program.
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program46.py 

# Choose your option:
# 1.Comparing with default values
# 2.Provide with new values
# 3.Exit
# Option: ;klhfs

# Error encountered, give the correct input or check the code
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$