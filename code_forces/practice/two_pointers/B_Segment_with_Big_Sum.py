n, s = map(int, input().split())
a = list(map(int, input().split()))

wn = 0
l = 0
res = n+1
for r in range(n):
    wn += a[r]
    while wn >= s:
        res = min(res, r-l+1)
        wn -= a[l]
        l += 1

print(res if res != n+1 else -1)
