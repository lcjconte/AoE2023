import sys, os, re
from math import floor, ceil, sqrt
nums = [list(map(lambda x: int(x), re.findall(re.compile(r"\d+"), i))) for i in sys.stdin.readlines()]
su = 1
for i in range(len(nums[0])):
    a, b = nums[0][i], nums[1][i]
    det = sqrt(a**2-4*b)
    lo, hi = (-a + det)/(-2), (-a - det)/(-2)
    lo = lo+1 if lo == ceil(lo) else ceil(lo)
    hi = hi-1 if hi == floor(hi) else floor(hi)
    su *= (hi-lo+1)
    # v(t-v) > m   - v^2 + vt - m > 0
print(su)