import random

def lmerger(l, a, b):
    if l[a] == l[b]:
        l[a] += l[b]
        l[b] = 0

def lmergeZero(l, a, b):
    if l[a] == 0:
        l[a] = l[b]
        l[b] = 0

def rmerger(l, a, b):
    if l[a] == l[b]:
        l[b] += l[a]
        l[a] = 0

def rmergeZero(l, a, b):
    if l[b] == 0:
        l[b] = l[a]
        l[a] = 0


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
    rmerger(row, 0, 1)
    rmerger(row, 1, 2)
    rmerger(row, 2, 3)

    rmergeZero(row, 0, 1)
    rmergeZero(row, 1, 2)
    rmergeZero(row, 2, 3)



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


showBoard()





        
