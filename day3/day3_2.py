import sys, re
from scipy.signal import convolve2d
import numpy as np
me = re.compile(r"\d+")
ex = lambda x: [int(i) for i in re.findall(me, x)]
lines = [list(i) for i in sys.stdin.read().splitlines()]
arr = np.array(lines)
gears = np.zeros(arr.shape)
for i in range(len(arr.flat)):
    gears.flat[i] = 1 if arr.flat[i] == "*" else 0
ngears = convolve2d(gears, np.ones((3, 3)), mode="same")
su = 0
nums = np.zeros(arr.shape)
for i, li in enumerate(lines):
    for mt in re.finditer(me, "".join(li)):
        nums[i,mt.start():mt.end()] = (1 if ngears[i, mt.start():mt.end()].sum() > 0 else 0) * int(mt.group())
for i in range(1, arr.shape[0]-1):
    for j in range(1, arr.shape[1]-1):
        if gears[i, j] == 0:
            continue
        nu = []
        for di in range(-1, 2):
            for dj in range(-1, 2):
                nu.append(nums[i+di, j+dj])
        nu = list(filter(lambda x: x != 0, set(nu)))
        if len(nu) == 2:
            su += nu[0]*nu[1]
print(su)