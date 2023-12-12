import sys, numpy as np
su = 0
rows = [] 
for line in sys.stdin.readlines():
    rows.append(line)
mp = np.array([[0 if j == "." else 1 for j in i.strip()] for i in rows])
nz = []
rval = np.full(mp.shape[0], 1_000_000)
cval = np.full(mp.shape[1], 1_000_000)
for i in range(mp.shape[0]):
    for j in range(mp.shape[1]):
        if mp[i, j] == 1:
            rval[i] = 1
            cval[j] = 1
            nz.append((i, j))
for idx, i in enumerate(nz):
    for j in nz[idx+1:]:
        x1, x2, y1, y2 = i[0], j[0], i[1] , j[1]
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        su += rval[x1:x2].sum() + cval[y1:y2].sum()
print(su)