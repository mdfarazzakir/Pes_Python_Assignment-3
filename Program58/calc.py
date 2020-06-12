"""Function to add two numbers"""
def add(num1,num2):
    return(num1 + num2)

"""Function to subtract two numbers"""
def subtract(num1,num2):
    return(num1 - num2)

"""Function to multiply two numbers"""
def multiply(num1,num2):
    return(num1 * num2)

"""Function to find the suare root of a number"""
def squareRoot(num):
    import math as m
    return(m.sqrt(num))

"""Function to divide two numbers with quotient as output"""
def divide(num1,num2):
    return(num1/num2)


"""Function to divide two numbers with remainder as output"""
def modulus(num1,num2):
    return(num1%num2)


"""Function to do floor division on two numbers"""
def floorDiv(num1,num2):
    return(num1//num2)


"""Function to find if the number is prime or not"""
def primeNumber(num):
    count = 0
    for i in range(2,num):
        if num%i == 0:
            count = 1

    if count == 1:
        print(num," is not a Prime number")
    else:
        print(num," is a prime number")


"""Function to generate fibonacci series"""
def fibo(num):
    n1 = 0
    n2 = 1
    for _ in range(num):
        print(n1)
        nxt = n1+n2
        n1 = n2
        n2=nxt