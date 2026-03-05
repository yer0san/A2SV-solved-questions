# horizontal prefix
pre = []
for _ in range(h+1):
    prep = [0]*(w+1)
    pre.append(prep)

# vertical prefix
pre2 = []
for _ in range(h+1):
    prep = [0]*(w+1)
    pre2.append(prep)

# horizontal
for i in range(1, h+1):
    for j in range(1, w+1):
        pre[i][j] += pre[i][j-1]

        if grid[i][j] == '.' and grid[i][j-1] == '.':
            pre[i][j] += 1

# vertical
for j in range(1, w+1):
    for i in range(1, h+1):
        pre2[i][j] += pre2[i-1][j]

        if grid[i][j] == '.' and grid[i-1][j] == '.':
            pre2[i][j] += 1


q = int(input())

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())

    ans = 0
    for i in range(r1, r2+1):
        ans += pre[i][c2] - pre[i][c1]

    for j in range(c1, c2+1):
        ans += pre2[r2][j] - pre2[r1][j]

    print(ans)