
su = 0
with open("./day1/input.txt") as f:
    for line in f.readlines():
        digits = []
        for c in line:
            try:
                digits.append(int(c))
            except:
                pass
        su += digits[0]*10+digits[-1]
print(su)