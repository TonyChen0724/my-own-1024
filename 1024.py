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
    #!!! Python don't have do...while... loop:
    coo1 = random.randrange(0, 4)
    coo2 = random.randrange(0, 4)
    while Matrix[coo1][coo2] != 0:
        coo1 = random.randrange(0, 4)
        coo2 = random.randrange(0, 4)
    Matrix[coo1][coo2] = 2

# print the board:
def showBoard():
    print("It's the new status!")
    for n in Matrix:
        print (n);

randomGenerator() 
showBoard()

# the reaction if input left, right, up and down:
#!!! about [0,0,2,4] --> [2,0,0,4] using while loop!!!

def left(row):
    condition1 = (row[3]-row[2]==row[3]) and (row[3] != 0)
    condition2 = (row[2]-row[1]==row[2]) and (row[2] != 0)
    condition3 = (row[1]-row[0]==row[1]) and (row[1] != 0)
    condition4 = (row[3] == row[2]) and (row[2] != 0) and (row[3] != 0)
    condition5 = (row[2] == row[1]) and (row[2] != 0) and (row[1] != 0)
    condition6 = (row[1] == row[0]) and (row[1] != 0) and (row[0] != 0)
 
    while condition1 or condition2 or condition3 or condition4 or condition5 or condition6:
        lmergeZero(row, 0, 1)
        lmergeZero(row, 1, 2)
        lmergeZero(row, 2, 3)

        lmerger(row, 2, 3)
        lmerger(row, 1, 2)
        lmerger(row, 0, 1)

        condition1 = (row[3]-row[2]==row[3]) and (row[3] != 0)
        condition2 = (row[2]-row[1]==row[2]) and (row[2] != 0)
        condition3 = (row[1]-row[0]==row[1]) and (row[1] != 0)
        condition4 = (row[3] == row[2]) and (row[2] != 0) and (row[3] != 0)
        condition5 = (row[2] == row[1]) and (row[2] != 0) and (row[1] != 0)
        condition6 = (row[1] == row[0]) and (row[1] != 0) and (row[0] != 0)
        
          
def right(row):
    condition1 = (row[2]-row[3]==row[2]) and (row[2] != 0)
    condition2 = (row[1]-row[2]==row[1]) and (row[1] != 0)
    condition3 = (row[0]-row[1]==row[0]) and (row[0] != 0)
    condition4 = (row[3] == row[2]) and (row[2] != 0) and (row[3] != 0)
    condition5 = (row[2] == row[1]) and (row[2] != 0) and (row[1] != 0)
    condition6 = (row[1] == row[0]) and (row[1] != 0) and (row[0] != 0)

    while condition1 or condition2 or condition3 or condition4 or condition5 or condition6:

        rmergeZero(row, 0, 1)
        rmergeZero(row, 1, 2)
        rmergeZero(row, 2, 3)

        rmerger(row, 0, 1)
        rmerger(row, 1, 2)
        rmerger(row, 2, 3)
        
        condition1 = (row[2]-row[3]==row[2]) and (row[2] != 0)
        condition2 = (row[1]-row[2]==row[1]) and (row[1] != 0)
        condition3 = (row[0]-row[1]==row[0]) and (row[0] != 0)
        condition4 = (row[3] == row[2]) and (row[2] != 0) and (row[3] != 0)
        condition5 = (row[2] == row[1]) and (row[2] != 0) and (row[1] != 0)
        condition6 = (row[1] == row[0]) and (row[1] != 0) and (row[0] != 0)


                



def top(lx, ly):
    zerotopmerger(lx, ly)
    twotopmerger(lx, ly)

def down(lx, ly):
    zerodownmerger(lx, ly)
    twodownmerger(lx, ly)

while True:


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
        condition1 = (Matrix[1][0] - Matrix[0][0] == Matrix[1][0] and Matrix[1][0] != 0)
        condition2 = (Matrix[2][0] - Matrix[1][0] == Matrix[2][0] and Matrix[2][0] != 0)
        condition3 = (Matrix[3][0] - Matrix[2][0] == Matrix[3][0] and Matrix[3][0] != 0)
        condition4 = (Matrix[1][0] == Matrix[0][0] and Matrix[1][0] != 0 and Matrix[0][0] != 0)
        condition5 = (Matrix[2][0] == Matrix[1][0] and Matrix[2][0] != 0 and Matrix[1][0] != 0)
        condition6 = (Matrix[3][0] == Matrix[2][0] and Matrix[3][0] != 0 and Matrix[2][0] != 0)
        condition7 = (Matrix[1][1] - Matrix[0][1] == Matrix[1][1] and Matrix[1][1] != 0)
        condition8 = (Matrix[2][1] - Matrix[1][1] == Matrix[2][1] and Matrix[2][1] != 0)
        condition9 = (Matrix[3][1] - Matrix[2][1] == Matrix[3][1] and Matrix[3][1] != 0)
        condition10 = (Matrix[1][1] == Matrix[0][1] and Matrix[1][1] != 0 and Matrix[0][1] != 0)
        condition11 = (Matrix[2][1] == Matrix[1][1] and Matrix[2][1] != 0 and Matrix[1][1] != 0)
        condition12 = (Matrix[3][1] == Matrix[2][1] and Matrix[3][1] != 0 and Matrix[2][1] != 0)
        condition13 = (Matrix[1][2] - Matrix[0][2] == Matrix[1][2] and Matrix[1][2] != 0)
        condition14 = (Matrix[2][2] - Matrix[1][2] == Matrix[2][2] and Matrix[2][2] != 0)
        condition15 = (Matrix[3][2] - Matrix[2][2] == Matrix[3][2] and Matrix[3][2] != 0)
        condition16 = (Matrix[1][2] == Matrix[0][2] and Matrix[1][2] != 0 and Matrix[0][2] != 0)
        condition17 = (Matrix[2][2] == Matrix[1][2] and Matrix[2][2] != 0 and Matrix[1][2] != 0)
        condition18 = (Matrix[3][2] == Matrix[2][2] and Matrix[3][2] != 0 and Matrix[2][2] != 0)
        condition19 = (Matrix[1][3] - Matrix[0][3] == Matrix[1][3] and Matrix[1][3] != 0)
        condition20= (Matrix[2][3] - Matrix[1][3] == Matrix[2][3] and Matrix[2][3] != 0)
        condition21 = (Matrix[3][3] - Matrix[2][3] == Matrix[3][3] and Matrix[3][3] != 0)
        condition22 = (Matrix[1][3] == Matrix[0][3] and Matrix[1][3] != 0 and Matrix[0][3] != 0)
        condition23 = (Matrix[2][3] == Matrix[1][3] and Matrix[2][3] != 0 and Matrix[1][3] != 0)
        condition24 = (Matrix[3][3] == Matrix[2][3] and Matrix[3][3] != 0 and Matrix[2][3] != 0)
        while(condition1 or condition2 or condition3 or condition4 or condition5 or condition6 or condition7 or condition8 or condition9 or condition10 or condition11 or condition12 or condition13 or condition14 or condition15 or condition16 or condition17 or condition18 or condition19 or condition20 or condition21 or condition22 or condition23 or condition24):

            top(Matrix[2], Matrix[3])
            top(Matrix[1], Matrix[2])
            top(Matrix[0], Matrix[1])

            condition1 = (Matrix[1][0] - Matrix[0][0] == Matrix[1][0] and Matrix[1][0] != 0)
            condition2 = (Matrix[2][0] - Matrix[1][0] == Matrix[2][0] and Matrix[2][0] != 0)
            condition3 = (Matrix[3][0] - Matrix[2][0] == Matrix[3][0] and Matrix[3][0] != 0)
            condition4 = (Matrix[1][0] == Matrix[0][0] and Matrix[1][0] != 0 and Matrix[0][0] != 0)
            condition5 = (Matrix[2][0] == Matrix[1][0] and Matrix[2][0] != 0 and Matrix[1][0] != 0)
            condition6 = (Matrix[3][0] == Matrix[2][0] and Matrix[3][0] != 0 and Matrix[2][0] != 0)
            condition7 = (Matrix[1][1] - Matrix[0][1] == Matrix[1][1] and Matrix[1][1] != 0)
            condition8 = (Matrix[2][1] - Matrix[1][1] == Matrix[2][1] and Matrix[2][1] != 0)
            condition9 = (Matrix[3][1] - Matrix[2][1] == Matrix[3][1] and Matrix[3][1] != 0)
            condition10 = (Matrix[1][1] == Matrix[0][1] and Matrix[1][1] != 0 and Matrix[0][1] != 0)
            condition11 = (Matrix[2][1] == Matrix[1][1] and Matrix[2][1] != 0 and Matrix[1][1] != 0)
            condition12 = (Matrix[3][1] == Matrix[2][1] and Matrix[3][1] != 0 and Matrix[2][1] != 0)
            condition13 = (Matrix[1][2] - Matrix[0][2] == Matrix[1][2] and Matrix[1][2] != 0)
            condition14 = (Matrix[2][2] - Matrix[1][2] == Matrix[2][2] and Matrix[2][2] != 0)
            condition15 = (Matrix[3][2] - Matrix[2][2] == Matrix[3][2] and Matrix[3][2] != 0)
            condition16 = (Matrix[1][2] == Matrix[0][2] and Matrix[1][2] != 0 and Matrix[0][2] != 0)
            condition17 = (Matrix[2][2] == Matrix[1][2] and Matrix[2][2] != 0 and Matrix[1][2] != 0)
            condition18 = (Matrix[3][2] == Matrix[2][2] and Matrix[3][2] != 0 and Matrix[2][2] != 0)
            condition19 = (Matrix[1][3] - Matrix[0][3] == Matrix[1][3] and Matrix[1][3] != 0)
            condition20= (Matrix[2][3] - Matrix[1][3] == Matrix[2][3] and Matrix[2][3] != 0)
            condition21 = (Matrix[3][3] - Matrix[2][3] == Matrix[3][3] and Matrix[3][3] != 0)
            condition22 = (Matrix[1][3] == Matrix[0][3] and Matrix[1][3] != 0 and Matrix[0][3] != 0)
            condition23 = (Matrix[2][3] == Matrix[1][3] and Matrix[2][3] != 0 and Matrix[1][3] != 0)
            condition24 = (Matrix[3][3] == Matrix[2][3] and Matrix[3][3] != 0 and Matrix[2][3] != 0)

    if direction == 'd':
       
        down(Matrix[0], Matrix[1])
        down(Matrix[1], Matrix[2])
        down(Matrix[2], Matrix[3])
    
    randomGenerator()
    showBoard()





        
