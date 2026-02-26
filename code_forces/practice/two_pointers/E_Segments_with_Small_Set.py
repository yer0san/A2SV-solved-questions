from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))

c = defaultdict(int)
res = 0
l = 0
for r in range(n):
    c[a[r]] += 1
    while len(c) > k:
        c[a[l]] -= 1
        if c[a[l]] == 0:
            del c[a[l]]
        l += 1
    res += r-l+1
print(res)