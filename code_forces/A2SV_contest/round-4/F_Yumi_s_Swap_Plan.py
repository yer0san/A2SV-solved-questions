n = int(input())
a = list(input())
ct = a.count('H')
a.extend(a)

mn = float('inf')
for i in range(n):
    seg = a[i:i+ct]
    tc = seg.count('T')
    mn = min(mn, tc)
print(mn)

