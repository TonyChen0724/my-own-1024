import random

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

showBoard()
randomGenerator()
showBoard()    

