from functools import lru_cache
import sys

cstring = ""
cl = []

@lru_cache(maxsize=None)
def crest(spos, rpos, cnt):
    if spos == len(cstring):
        if rpos != len(cl)-1:
            return 0
        return 1
    match cstring[spos]:
        case ".":
            return doa(spos, rpos, cnt)
        case "#":
            return dob(spos, rpos, cnt)
        case "?":
            return doa(spos, rpos, cnt)+dob(spos, rpos, cnt)

def doa(spos, rpos, cnt):
    if cnt > 0 and cnt != cl[rpos]:
        return 0
    return crest(spos+1, rpos + (1 if cnt > 0 else 0), 0) 

def dob(spos, rpos, cnt):
    if cnt == cl[rpos]:
        return 0
    return crest(spos+1, rpos, cnt+1)
su = 0
for line in sys.stdin.readlines():
    ostring, x = line.strip().split(" ")
    cstring = 5*(ostring+"?")
    cstring = cstring[:-1]+"."
    cl = 5*[int(i) for i in x.split(",")]+[0]
    su += crest(0,0,0)
    crest.cache_clear()
print(su)