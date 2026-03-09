n, b = map(int, input().split())
a = list(map(int, input().split()))

valids = []
ec = 0
oc = 0

for i, num in enumerate(a[:n-1]):
    if num%2 == 0:
        ec += 1
    else:
        oc += 1
    if ec == oc:
        valids.append(abs(num-a[i+1]))

valids.sort()
res = 0
for v in valids:
    b -= v
    if b >= 0:
        res += 1
print(res)

