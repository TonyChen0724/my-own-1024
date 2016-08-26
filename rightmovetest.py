def rmerger(l, a, b):
    if l[a] == l[b]:
        l[b] += l[a]
        l[a] = 0

def rmergeZero(l, a, b):
    if l[b] == 0:
        l[b] = l[a]
        l[a] = 0


row = [0, 2, 4, 4] # it's what passing as a parameter
rmerger(row, 0, 1)
rmerger(row, 1, 2)
rmerger(row, 2, 3)

rmergeZero(row, 0, 1)
rmergeZero(row, 1, 2)
rmergeZero(row, 2, 3)



print (row)



