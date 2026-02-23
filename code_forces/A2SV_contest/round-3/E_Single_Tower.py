n = int(input())
towers = []
sor = []
for _ in range(n):
    t = list(map(int, input().split()))
    towers.append(t[1::])
    sor += t[1::]

sor.sort()
mapper = {val: i for i, val in enumerate(sor)}

s = 0
for i in range(len(towers)):
    for j in range(1, len(towers[i])):
        if mapper[towers[i][j]] != mapper[towers[i][j-1]]+1:
            s += 1

print(s, len(towers)+s-1)