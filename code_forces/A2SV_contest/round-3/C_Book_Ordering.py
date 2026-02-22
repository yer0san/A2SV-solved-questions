n = int(input())
a = []
for _ in range(n):
    w, h = map(int, input().split())
    a.append([w, h])

no = False
prev = max(a[0][0], a[0][1])
for w, h in a:
    now = max(w, h)
    if now <= prev:
        prev = now
        continue
    now = min(w, h)
    if now <= prev:
        prev = now
        continue
    no = True
    break

if no:
    print('NO')
else:
    print('YES')
    