ne = {}
import sys
for i, li in enumerate(sys.stdin.readlines()):
    if i == 0:
        inst = li.strip()
        continue
    elif i == 1:
        continue
    a, b = li.strip().split(" = ")
    ne[a] = b[1:-1].split(", ")
cn = "AAA"
cmin = 1e12
i = 0
print("Starting process")
current = [(xx, xx) for xx in ne.keys() if xx[-1] == "A"]
occs = {xx:[] for xx in current}
while len(current) > 0:
    ncur = []
    for cn in current:
        ncur.append((cn[0], ne[cn[1]][0 if inst[i % len(inst)] == "L" else 1]))
    current = ncur
    i += 1
    val = True
    for no in current:
        if no[1][-1] == "Z":
            if in occs[no[0]]
            occs[no[0]].append(i)
        if no[-1] != "Z":
            val = False
    if val:
        cmin = i
        break
print(cmin)