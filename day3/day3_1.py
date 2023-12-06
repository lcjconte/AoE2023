import sys, re
from scipy.signal import convolve2d
import numpy as np
me = re.compile(r"\d+")
ex = lambda x: [int(i) for i in re.findall(me, x)]
lines = [list(i) for i in sys.stdin.read().splitlines()]
arr = np.array(lines)
narr = np.zeros(arr.shape)
for i in range(len(arr.flat)):
    narr.flat[i] = 1 if arr.flat[i] not in [str(i) for i in range(10)]+["."] else 0
narr = convolve2d(narr, np.ones((3, 3)), mode="same")
su = 0
for i, li in enumerate(lines):
    for mt in re.finditer(me, "".join(li)):
        su += (1 if narr[i, mt.start():mt.end()].sum() > 0 else 0) * int(mt.group())
print(su)