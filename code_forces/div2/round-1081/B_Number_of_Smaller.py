# not in here
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
j = 0
res = []
for i in range(len(b)):
    while j < len(a) and a[j] < b[i]:
        j += 1
    res.append(j)
print(*res)
