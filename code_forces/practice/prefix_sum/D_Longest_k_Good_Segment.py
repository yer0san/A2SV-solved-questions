from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int,input().split()))


l = 0
res = [1, 1]
mapper = defaultdict(int)
mx = 0

for r in range(n):
    mapper[a[r]] += 1
    if len(mapper) > k:
        mapper[a[l]] -= 1
        if mapper[a[l]] <= 0:
            del mapper[a[l]]
        l += 1

    if mx < r-l:
        mx = r-l
        res[0] = l+1
        res[1] = r+1

print(*res)
