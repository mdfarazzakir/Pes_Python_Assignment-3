"""
Functions:
Write a program to generate a Fibonacci series using a function called fib(n), 
a) Where ‘n’ is user specified argument specifies number of elements in the series.
"""

"""To pass the positional arguments in the function we have used *arg which acts as the representator for
 the arguments being input in the function"""
def fibo(*arg):
       
    n1 = 1
    n2 = 1
    for _ in range(*arg):
        yield n1
        n1,n2 = n2,n1+n2
    

number = eval(input("Enter the number to generate Fibonacci series: "))
for num in fibo(number):
    print(num)



# Output:
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program42.py 
# Enter the number to generate Fibonacci series: 10
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
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program42.py 
# Enter the number to generate Fibonacci series: 25
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
# 89
# 144
# 233
# 377
# 610
# 987
# 1597
# 2584
# 4181
# 6765
# 10946
# 17711
# 28657
# 46368
# 75025
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$