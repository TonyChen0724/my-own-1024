def merger(l, a, b):
    if l[a] == l[b]:
        l[a] += l[b]
        l[b] = 0

def mergeZero(l, a, b):
    if l[a] == 0:
        l[a] = l[b]
        l[b] = 0


row = [0, 2, 4, 4] # it's what passing as a parameter
merger(row, 2, 3)
merger(row, 1, 2)
merger(row, 0, 1)

mergeZero(row, 2, 3)
mergeZero(row, 1, 2)
mergeZero(row, 0, 1)



print (row)



