"""
Functions:
Write a program to search given element from the list. Use your own function to search an element from list.
Note: Function should receive variable length arguments and search each of these arguments present in 
the list.

"""

def binarySearch(sortedList,lower,upper,searchTerm):
    global middle
    while lower<=upper:
        middle = (lower+upper)//2
        if sortedList[middle]==searchTerm:
            return middle
        elif sortedList[middle]<searchTerm:
            lower = middle+1
        else:
            upper = middle-1
    return 0


"""Using try and except block for error handling"""
try:
    """Generating list of number from 1 to 100 in sorted form"""
    sortedList = list()
    listLimit = int(input("Enter the limit: "))
    for i in range(listLimit):
        numbers = int(input("Enter the numbers in ascending order: "))
        sortedList.append(numbers)


    """Setting up the lower, middle and upper limit"""
    lower = 0
    upper = len(sortedList)-1
    middle = int()


    searchTerm = int(input("Enter the number you want to search from the list: "))


    """Calling the function"""
    result = binarySearch(sortedList,lower,upper,searchTerm)

    if result==0:
        print("Number %d not found in the list."%searchTerm)
    else:
        print("Number %d found in the list at position %d"%(searchTerm,middle+1))
except:
    print("Error encountered, please give a valid input or check the code.")

# Output:
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ python3 Program43.py
# Enter the limit: 10
# Enter the numbers in ascending order: 20
# Enter the numbers in ascending order: 24
# Enter the numbers in ascending order: 25
# Enter the numbers in ascending order: 27
# Enter the numbers in ascending order: 28
# Enter the numbers in ascending order: 31
# Enter the numbers in ascending order: 33
# Enter the numbers in ascending order: 35
# Enter the numbers in ascending order: 36
# Enter the numbers in ascending order: 37
# Enter the number you want to search from the list: 31
# Number 31 found in the list at position 6
# rgolem@golem:~/Desktop/Python/Pes_Python_Assignments-3$ 