n, s = map(int, input().split())
a = list(map(int, input().split()))

wn = 0
l = 0



res = 0
for r in range(n):
    wn += a[r]
    while wn >= s:
        res += n-r
        wn -= a[l]
        l += 1

print(res)