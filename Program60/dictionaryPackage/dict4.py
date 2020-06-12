"""
Dictionary  and Date & Time:
Using time module perform following operations.
a) Print current time for every 5 seconds up to 1 minute time interval.
"""
import time
from datetime import datetime as dt


n = dt.now()
ct = n.strftime("%H:%M:%S")
start_time = int(time.time())
print("\na)Printing current time for every 5 seconds:")
for i in range(0,60+5):
    time.sleep(1)
    if i%5 == 0:
        print("\nAfter %s seconds"%i)
        print(ct)
    else:
        print("\n",i)


# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program40a.py
#
# a)Printing current time for every 5 seconds:
#
# After 0 seconds
# 19:04:26
#
#  1
#
#  2
#
#  3
#
#  4
#
# After 5 seconds
# 19:04:26
#
#  6
#
#  7
#
#  8
#
#  9
#
# After 10 seconds
# 19:04:26
#
#  11
#
#  12
#
#  13
#
#  14
#
# After 15 seconds
# 19:04:26
#
#  16
#
#  17
#
#  18
#
#  19
#
# After 20 seconds
# 19:04:26
#
#  21
#
#  22
#
#  23
#
#  24
#
# After 25 seconds
# 19:04:26
#
#  26
#
#  27
#
#  28
#
#  29
#
# After 30 seconds
# 19:04:26
#
#  31
#
#  32
#
#  33
#
#  34
#
# After 35 seconds
# 19:04:26
#
#  36
#
#  37
#
#  38
#
#  39
#
# After 40 seconds
# 19:04:26
#
#  41
#
#  42
#
#  43
#
#  44
#
# After 45 seconds
# 19:04:26
#
#  46
#
#  47
#
#  48
#
#  49
#
# After 50 seconds
# 19:04:26
#
#  51
#
#  52
#
#  53
#
#  54
#
# After 55 seconds
# 19:04:26
#
#  56
#
#  57
#
#  58
#
#  59
#
# After 60 seconds
# 19:04:26
#
#  61
#
#  62
#
#  63
#
#  64
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
