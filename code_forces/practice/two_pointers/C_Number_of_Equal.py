n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = 0
prev = 0
prevn = a[0]
j = 0
for i in range(n):

    if j < m and a[i] > b[j]:
        while j < m and a[i] > b[j]:
                j += 1
    if j < m and a[i] == b[j]:
        prev = 0
        prevn = a[i]
        while j < m and a[i] == b[j]:
            res += 1
            prev += 1
            j += 1
        continue

    else:
        if prevn == a[i]:
            res += prev
        
print(res)
