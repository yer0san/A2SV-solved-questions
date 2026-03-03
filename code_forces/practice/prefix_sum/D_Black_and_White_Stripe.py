# sliding window
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = input()

    seg = a[:k]
    res = seg.count('W')
    l = 0
    cur = res
    for r in range(k, n):
        if a[r] == 'W':
            cur += 1
        if a[l] == 'W':
            cur -= 1
        res = min(res, cur)
        l += 1
    print(res)