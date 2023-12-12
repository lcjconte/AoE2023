import sys
su = 0
for line in sys.stdin.readlines():
    nums = [[int(i) for i in line.split(" ")]]
    while sum([abs(i) for i in nums[-1]]) > 0:
        nums.append([])
        for i in range(len(nums[-2])-1):
            nums[-1].append(nums[-2][i+1]-nums[-2][i])
    while len(nums) > 1:
        nums[-2].append(nums[-2][-1]+nums[-1][-1])
        nums.pop(-1)
    su += nums[-1][-1]
print(su)