def twomerger(lx, ly):
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

def zeromerger(lx, ly):
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

def tmerger(lx, ly):
    zeromerger(lx, ly)
    twomerger(lx, ly)

row1 = [0, 2, 4, 4]
row2 = [2, 2, 4, 4]

print (row1)
print (row2)
tmerger(row1, row2)
print ("it's a new situation:")
print (row1)
print (row2)




