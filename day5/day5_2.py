import sys, re
me = re.compile(r"\d+")
ex = lambda x: [int(i) for i in re.findall(me, x)]
lines = sys.stdin.read().split(":")[1:]
nums = [ex(li) for li in lines]
ranges = sorted([nums[0][i:i+2] for i in range(0, len(nums[0]), 2)])
for i in range(1, len(nums)):
    blocks = sorted([nums[i][j+1:j+2]+nums[i][j:j+3] for j in range(0, len(nums[i]), 3)])
    #Uni ranges
    nra = []
    while len(ranges) > 0:
        while len(ranges) > 1 and ranges[0][0]+ranges[0][1] >= ranges[1][0]:
            ranges[1] = [ranges[0][0], max([ranges[0][1], (ranges[1][0]-ranges[0][0])+ranges[1][1]])]
            ranges.pop(0)
        nra.append(ranges.pop(0))
    nitems = []
    if blocks[0][0] != 0:
        blocks.insert(0, [0, 0, blocks[0][0]])
    blocks.append([blocks[-1][0]+blocks[-1][-1], blocks[-1][0]+blocks[-1][-1], 1_000_000_000])
    for r in nra:
        while blocks[0][0]+blocks[0][-1] <= r[0]:
            blocks.pop(0)
        for bl in blocks:
            if bl[0] >= r[0]+r[1]:
                break
            lo = max([bl[0], r[0]])
            hi = min([bl[0]+bl[-1], r[0]+r[1]])
            nitems.append([bl[1]+(lo-bl[0]), hi-lo])
    ranges = sorted(nitems)
print(min([i[0] for i in ranges]))