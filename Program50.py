"""
File I/O Operations:
Write a program to open the existing file in read mode and perform following tasks,
a) Read 10 character at a time and then print its current position of file object. Repeat this operation till the EOF.
b) Reset the file pointer after reading 100 Character from file (Use Seek function to reset)
c) Open the file in read mode and start printing the contents from 5th line onwards.
"""

"""a)Function to read 10 character at a time and then print its current position of file object."""
def read10Char(file):
    fopen = open(file,mode='r')

    filePointer = 0
    while True:
        line  = fopen.read(10)
        if not line:
            break
        else:
            print("\n10 Charaters including whitespace: ",line)
            filePointer +=10
            print("\nPointer at position: ",filePointer)

def resetAfter100(file):
    fopen = open(file,mode='r')
    filePointer = 0
    while filePointer<100:
        line = fopen.read(10)
        if not line:
            break
        else:
            print("\n10 Chraters including whitespace: ",line)
            filePointer +=10
            print("\nPointer at position: ",filePointer)
    filePointer = fopen.seek(0)
    print("\nPointer has been reseted")
    print("\nPointer position at :",filePointer)


def readAfter5(file):
    fopen = open(file,mode='r')
    f1 = enumerate(fopen,1)
    for i in f1:
        if i[0]>4:
            i = list(i)
            i[0] = str(i[0])+'.'
            j = "".join(i)
            print(j) 


file = input("Enter the file name you want to open: ")

print("\na)Reading and printing 10 characters at a time and printing the Pointer position:\n")
read10Char(file)

print("\nb)Reading and printing 10 characters at a time and printing the Pointer position and after 100 charecters the pointer will reset:\n")
resetAfter100(file)

print("\nc)Reading and printing characters from 5th line onwards:\n")
readAfter5(file)


# Output:
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>python Program50.py
# Enter the file name you want to open: Program50Data.txt

# a)Reading and printing 10 characters at a time and printing the Pointer position:


# 10 Charaters including whitespace:  These line

# Pointer at position:  10

# 10 Charaters including whitespace:  s are writ

# Pointer at position:  20

# 10 Charaters including whitespace:  ten in wri

# Pointer at position:  30

# 10 Charaters including whitespace:  te mode
# Th

# Pointer at position:  40

# 10 Charaters including whitespace:  e previous

# Pointer at position:  50

# 10 Charaters including whitespace:   data has

# Pointer at position:  60

# 10 Charaters including whitespace:  been erase

# Pointer at position:  70

# 10 Charaters including whitespace:  d as the f

# Pointer at position:  80

# 10 Charaters including whitespace:  ile has be

# Pointer at position:  90

# 10 Charaters including whitespace:  en created

# Pointer at position:  100

# 10 Charaters including whitespace:   newly
# The

# Pointer at position:  110

# 10 Charaters including whitespace:   quick bro

# Pointer at position:  120

# 10 Charaters including whitespace:  wn fox
# jum

# Pointer at position:  130

# 10 Charaters including whitespace:  ps over
# th

# Pointer at position:  140

# 10 Charaters including whitespace:  e lazy dog

# Pointer at position:  150

# 10 Charaters including whitespace:
# These bel

# Pointer at position:  160

# 10 Charaters including whitespace:  ow line ar

# Pointer at position:  170

# 10 Charaters including whitespace:  e written

# Pointer at position:  180

# 10 Charaters including whitespace:  in append

# Pointer at position:  190

# 10 Charaters including whitespace:  mode
# New l

# Pointer at position:  200

# 10 Charaters including whitespace:  ines will

# Pointer at position:  210

# 10 Charaters including whitespace:  be added b

# Pointer at position:  220

# 10 Charaters including whitespace:  elow the l

# Pointer at position:  230

# 10 Charaters including whitespace:  ines that

# Pointer at position:  240

# 10 Charaters including whitespace:  were writt

# Pointer at position:  250

# 10 Charaters including whitespace:  en previou

# Pointer at position:  260

# 10 Charaters including whitespace:  sly
# The se

# Pointer at position:  270

# 10 Charaters including whitespace:  ntence, Th

# Pointer at position:  280

# 10 Charaters including whitespace:  e quick br

# Pointer at position:  290

# 10 Charaters including whitespace:  own fox ju

# Pointer at position:  300

# 10 Charaters including whitespace:  mps over t

# Pointer at position:  310

# 10 Charaters including whitespace:  he lazy do

# Pointer at position:  320

# 10 Charaters including whitespace:  g
# ,contain

# Pointer at position:  330

# 10 Charaters including whitespace:  s all the

# Pointer at position:  340

# 10 Charaters including whitespace:  letters of

# Pointer at position:  350

# 10 Charaters including whitespace:   the Engli

# Pointer at position:  360

# 10 Charaters including whitespace:  sh Alphabe

# Pointer at position:  370

# 10 Charaters including whitespace:  t
# All 26 l

# Pointer at position:  380

# 10 Charaters including whitespace:  etter

# Pointer at position:  390

# b)Reading and printing 10 characters at a time and printing the Pointer position and after 100 charecters the pointer will reset:


# 10 Chraters including whitespace:  These line

# Pointer at position:  10

# 10 Chraters including whitespace:  s are writ

# Pointer at position:  20

# 10 Chraters including whitespace:  ten in wri

# Pointer at position:  30

# 10 Chraters including whitespace:  te mode
# Th

# Pointer at position:  40

# 10 Chraters including whitespace:  e previous

# Pointer at position:  50

# 10 Chraters including whitespace:   data has

# Pointer at position:  60

# 10 Chraters including whitespace:  been erase

# Pointer at position:  70

# 10 Chraters including whitespace:  d as the f

# Pointer at position:  80

# 10 Chraters including whitespace:  ile has be

# Pointer at position:  90

# 10 Chraters including whitespace:  en created

# Pointer at position:  100

# Pointer has been reseted

# Pointer position at : 0

# c)Reading and printing characters from 5th line onwards:

# 5.the lazy dog

# 6.These below line are written in append mode

# 7.New lines will be added below the lines that were written previously

# 8.The sentence, The quick brown fox jumps over the lazy dog

# 9.,contains all the letters of the English Alphabet

# 10.All 26 letter

# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignments-3>