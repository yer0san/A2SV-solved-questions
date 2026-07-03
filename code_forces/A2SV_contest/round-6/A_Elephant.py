# not in the contest
x = int(input())

y = 5
res = 0
while x > 0:
    if x >= y:
        x -= y
        res += 1
    else:
        y -= 1
print(res)