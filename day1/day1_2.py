mp = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
su = 0
with open("./day1/input.txt") as f:
    for line in f.readlines():
        digits = []
        for i in range(len(line)):
            for k in mp.keys():
                if k in line[i:min([i+len(k), len(line)])]:
                    digits.append(mp[k])
                    continue
            try:
                digits.append(int(line[i]))
            except:
                pass
        su += digits[0]*10+digits[-1]
print(su)