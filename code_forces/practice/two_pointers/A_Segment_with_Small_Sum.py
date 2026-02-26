n, s = map(int, input().split())
a = list(map(int, input().split()))

res = 0
wind = 0
left = 0
for r in range(n):
    wind += a[r]
    while wind > s:
        wind -= a[left]
        left += 1
    res = max(res, r-left+1)

print(res)


