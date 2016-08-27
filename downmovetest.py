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

def dmerger(lx, ly):
    zerodownmerger(lx, ly)
    twodownmerger(lx, ly)

row1 = [0, 2, 4, 4]
row2 = [2, 2, 4, 4]

print (row1)
print (row2)
dmerger(row1, row2)
print ("it's a new situation:")
print (row1)
print (row2)




