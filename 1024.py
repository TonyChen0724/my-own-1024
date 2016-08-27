import random

# left merger:
def lmerger(l, a, b):
    if l[a] == l[b]:
        l[a] += l[b]
        l[b] = 0

def lmergeZero(l, a, b):
    if l[a] == 0:
        l[a] = l[b]
        l[b] = 0

# right merger:
def rmerger(l, a, b):
    if l[a] == l[b]:
        l[b] += l[a]
        l[a] = 0

def rmergeZero(l, a, b):
    if l[b] == 0:
        l[b] = l[a]
        l[a] = 0

# top merger:
def twotopmerger(lx, ly):
    if lx[0] == ly[0]:
        lx[0] += ly[0]
        ly[0] = 0
    if lx[1] == ly[1]:
        lx[1] += ly[1]
        ly[1] = 0
    if lx[2] == ly[2]:
        lx[2] += ly[2]
        ly[2] = 0
    if lx[3] == ly[3]:
        lx[3] += ly[3]
        ly[3] = 0

def zerotopmerger(lx, ly):
    if lx[0] == 0:
        lx[0] += ly[0]
        ly[0] = 0
    if lx[1] == 0:
        lx[1] += ly[1]
        ly[1] = 0
    if lx[2] == 0:
        lx[2] += ly[2]
        ly[2] = 0
    if lx[3] == 0:
        lx[3] += ly[3]
        ly[3] = 0

# down merge:
def twodownmerger(lx, ly):
    if lx[0] == ly[0]:
        ly[0] += lx[0]
        lx[0] = 0
    if lx[1] == ly[1]:
        ly[1] += lx[1]
        lx[1] = 0
    if lx[2] == ly[2]:
        ly[2] += lx[2]
        lx[2] = 0
    if lx[3] == ly[3]:
        ly[3] += lx[3]
        lx[3] = 0

def zerodownmerger(lx, ly):
    if ly[0] == 0:
        ly[0] += lx[0]
        lx[0] = 0
    if ly[1] == 0:
        ly[1] += lx[1]
        lx[1] = 0
    if ly[2] == 0:
        ly[2] += lx[2]
        lx[2] = 0
    if ly[3] == 0:
        ly[3] += lx[3]
        lx[3] = 0


w = 4
h = 4
Matrix = [[0 for x in range(w)] for y in range(h)]
# ^generate a 4*4 matrix

# generate 2 in a random block:
def randomGenerator():
    coo1 = random.randrange(0, 4)
    coo2 = random.randrange(0, 4)
    Matrix[coo1][coo2] = 2;

# print the board:
def showBoard():
    print("It's the new status!")
    for n in Matrix:
        print (n);

randomGenerator() 
showBoard()

# the reaction if input left, right, up and down:
def left(row):
    lmergeZero(row, 2, 3)
    lmergeZero(row, 1, 2)
    lmergeZero(row, 0, 1)

    lmerger(row, 2, 3)
    lmerger(row, 1, 2)
    lmerger(row, 0, 1)

def right(row):
    rmergeZero(row, 0, 1)
    rmergeZero(row, 1, 2)
    rmergeZero(row, 2, 3)

    rmerger(row, 0, 1)
    rmerger(row, 1, 2)
    rmerger(row, 2, 3)

def top(lx, ly):
    zerotopmerger(lx, ly)
    twotopmerger(lx, ly)

def down(lx, ly):
    zerodownmerger(lx, ly)
    twodownmerger(lx, ly)

direction = input()


if direction == 'l':
    left(Matrix[0])
    left(Matrix[1])
    left(Matrix[2])
    left(Matrix[3])

if direction == 'r':
    right(Matrix[0])
    right(Matrix[1])
    right(Matrix[2])
    right(Matrix[3])

if direction == 't':
    top(Matrix[2], Matrix[3])
    top(Matrix[1], Matrix[2])
    top(Matrix[0], Matrix[1])

if direction == 'd':
    down(Matrix[0], Matrix[1])
    down(Matrix[1], Matrix[2])
    down(Matrix[2], Matrix[3])

showBoard()





        
