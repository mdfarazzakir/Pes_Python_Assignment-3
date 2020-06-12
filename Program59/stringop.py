"""Function for Buuble Sort"""
def bubbleSort(num):
    temp = 0
    for i in range(0,len(num)):
        for j in range(0,len(num)):
            if num[i]<num[j]:
                temp = num[i]
                num[i] = num[j]
                num[j] = temp

    return(num)

"""Function for Binary Search"""
def binarySearch(sortedList,lower,upper,searchTerm):
#         global middle
    while lower<=upper:
        middle = (lower+upper)//2
        if sortedList[middle]==searchTerm:
            return middle
        elif sortedList[middle]<searchTerm:
            lower = middle+1
        else:
            upper = middle-1
    return 0


"""Function for String Reversal"""
def strgReverse(strg):
    """Length of the string"""
    sL = len(strg)

    """Intializing a variable as string"""
    strg1 = str()

    for i in range(sL-1,-1,-1):
        strg1 = strg1 + strg[i]
    return(strg1)


