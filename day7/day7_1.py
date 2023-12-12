import sys
mp = {
    "A": 24,
    "K": 23,
    "Q": 22,
    "J": 21,
    "T": 20
}
mp.update({str(i): i for i in range(2, 10)})
def spec(a):
    if len(set(a)) == 1:
        return 10
    if len(set(a)) == 2 and a.count(a[0]) in [1, 4]:
        return 9
    if len(set(a)) == 2:
        return 8
    for i in a:
        if a.count(i) == 3:
            return 7
    cnt = 0
    for i in a:
        if a.count(i) == 2:
            cnt += 1
    if cnt == 4:
        return 6
    if cnt == 2:
        return 5
    return 4
def score(a):
    sc = [spec(a)]
    for i in a:
        sc.append(mp[i])
    return sc
items = []
for line in sys.stdin.readlines():
    items.append(line.split(" "))
    items[-1].insert(0, score(items[-1][0]))
items.sort()
su = 0
for i, it in enumerate(items):
    su += (i+1)*int(it[-1])
print(su)