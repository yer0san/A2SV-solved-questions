t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    x = input().strip()
    s = input().strip()

    ops = 0

    while len(x) < m:
        x += x
        ops += 1

    if s in x:
        print(ops)
        continue

    x += x
    ops += 1
    if s in x:
        print(ops)
        continue

    x += x
    ops += 1
    if s in x:
        print(ops)
    else:
        print(-1)