import sys, os
sys.path.append(os.path.abspath("."))
from utils import lines
import re
su = 0
mp = {0: 1}
lins = list(lines())
mp = {i: 1 for i in range(len(lins))}
for i, li in enumerate(lins):
    #if i not in mp.keys() or mp[i] == 0:
    #    break
    me = re.compile(r"\d{1,2}")
    a, b = li.split(":")[1].split("|")
    cnt = len(set(re.findall(me, a)).intersection(re.findall(me, b)))
    for j in range(i+1, i+cnt+1):
        if j not in mp.keys():
            mp[j] = 0
        mp[j] += mp[i]
    su += 2**(cnt-1) if cnt > 0 else 0
print(sum(mp.values()))