import sys, re
me = re.compile(r"\d+")
ex = lambda x: [int(i) for i in re.findall(me, x)]
lines = sys.stdin.read().split(":")[1:]
nums = [ex(li) for li in lines]
items = sorted(nums[0])
for i in range(1, len(nums)):
    blocks = sorted([nums[i][j+1:j+2]+nums[i][j:j+3] for j in range(0, len(nums[i]), 3)])
    nitems = []
    for n in items:
        if len(blocks) == 0 or n < blocks[0][0]:
            nitems.append(n)
            continue
        while len(blocks) > 0 and n-blocks[0][0] >= blocks[0][-1]:
            blocks.pop(0)
        if len(blocks) == 0:
            nitems.append(n)
            continue
        nitems.append(blocks[0][1]+n-blocks[0][0])
    items = sorted(nitems)
print(min(items))