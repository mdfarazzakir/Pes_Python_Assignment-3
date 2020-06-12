"""
File I/O Operations:
Open existing text file and reverse its contents. i.e
a) print the last line as first line and first line as last line (Reverse the lines of the file)
b) print characters of file from last character of file till the first character of the file.
(Reverse entire contents of  file )
"""

file  = 'Program52Data.txt'

"""a)printing the last line as first line and first line as last line (Reverse the lines of the file)"""
print("Reversing the file ",file)
fopen = reversed(open(file).readlines())
for line in fopen:
    print(line)


"""b)printing characters of file from last character of file till the first character of the file.
(Reverse entire contents of  file )"""
print("Printing charecters of file from last till first in reverse manner of the tha file ",file)
print("Reversing the lines and printing the charecters of file",file)
fopen = list(reversed(open(file).read()))
# for charecters in fopen:
    # print(charecters)
print(fopen)


# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>python Program52.py
# Reversing the file  Program52Data.txt
# All 26 letter
# ,contains all the letters of the English Alphabet

# The sentence, The quick brown fox jumps over the lazy dog

# New lines will be added below the lines that were written previously

# These below line are written in append mode

# the lazy dog

# jumps over

# The quick brown fox

# The previous data has been erased as the file has been created newly

# These lines are written in write mode

# Printing charecters of file from last till first in reverse manner of the tha file  Program52Data.txt
# Reversing the lines and printing the charecters of file Program52Data.txt
# ['r', 'e', 't', 't', 'e', 'l', ' ', '6', '2', ' ', 'l', 'l', 'A', '\n', 't', 'e', 'b', 'a', 'h', 'p', 'l', 'A', ' ', 'h', 's', 'i', 'l', 'g', 'n', 'E', ' ', 'e', 'h', 't', ' ', 'f', 'o', ' ', 's', 'r', 'e', 't', 't', 'e', 'l', ' ', 'e', 'h', 't', ' ', 'l', 'l', 'a', ' ', 's', 'n', 'i', 'a', 't', 'n', 
# 'o', 'c', ',', '\n', 'g', 'o', 'd', ' ', 'y', 'z', 'a', 'l', ' ', 'e', 'h', 't', ' ', 'r', 'e', 'v', 'o', ' ', 's', 'p', 'm', 'u', 'j', ' ', 'x', 'o', 
# 'f', ' ', 'n', 'w', 'o', 'r', 'b', ' ', 'k', 'c', 'i', 'u', 'q', ' ', 'e', 'h', 'T', ' ', ',', 'e', 'c', 'n', 'e', 't', 'n', 'e', 's', ' ', 'e', 'h', 'T', '\n', 'y', 'l', 's', 'u', 'o', 'i', 'v', 'e', 'r', 'p', ' ', 'n', 'e', 't', 't', 'i', 'r', 'w', ' ', 'e', 'r', 'e', 'w', ' ', 't', 'a', 'h', 't', ' ', 's', 'e', 'n', 'i', 'l', ' ', 'e', 'h', 't', ' ', 'w', 'o', 'l', 'e', 'b', ' ', 'd', 'e', 'd', 'd', 'a', ' ', 'e', 'b', ' ', 'l', 'l', 'i', 'w', ' 
# ', 's', 'e', 'n', 'i', 'l', ' ', 'w', 'e', 'N', '\n', 'e', 'd', 'o', 'm', ' ', 'd', 'n', 'e', 'p', 'p', 'a', ' ', 'n', 'i', ' ', 'n', 'e', 't', 't', 'i', 'r', 'w', ' ', 'e', 'r', 'a', ' ', 'e', 'n', 'i', 'l', ' ', 'w', 'o', 'l', 'e', 'b', ' ', 'e', 's', 'e', 'h', 'T', '\n', 'g', 'o', 'd', ' ', 'y', 'z', 'a', 'l', ' ', 'e', 'h', 't', '\n', 'r', 'e', 'v', 'o', ' ', 's', 'p', 'm', 'u', 'j', '\n', 'x', 'o', 'f', ' ', 'n', 'w', 'o', 'r', 'b', ' ', 'k', 'c', 'i', 'u', 'q', ' ', 'e', 'h', 'T', '\n', 'y', 'l', 'w', 'e', 'n', ' ', 'd', 'e', 't', 'a', 'e', 'r', 'c', ' ', 'n', 'e', 'e', 'b', ' ', 's', 'a', 'h', ' ', 'e', 'l', 'i', 'f', ' ', 'e', 'h', 't', ' ', 's', 'a', ' ', 'd', 'e', 's', 'a', 'r', 'e', ' ', 'n', 'e', 'e', 'b', ' ', 's', 'a', 'h', ' ', 'a', 't', 'a', 'd', ' ', 's', 'u', 'o', 'i', 'v', 'e', 'r', 'p', ' ', 'e', 'h', 'T', '\n', 'e', 'd', 'o', 'm', ' ', 'e', 't', 'i', 'r', 'w', ' ', 'n', 'i', ' ', 'n', 'e', 't', 't', 'i', 'r', 'w', ' ', 'e', 'r', 'a', ' ', 's', 'e', 'n', 'i', 'l', ' ', 'e', 's', 'e', 'h', 'T']