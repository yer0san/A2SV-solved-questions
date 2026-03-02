from collections import Counter
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    c = Counter(a)
    b = sorted(c)

    res = 0
    l = 0
    wn = 0
    wn_c = 0
    for r in range(len(b)):
        wn += c[b[r]]
        wn_c += 1

        while wn_c > k:
            wn_c -= 1
            wn -= c[b[l]]
            l += 1

        res = max(res, wn)
        if b[r]+1 not in c:
            wn = 0
            wn_c = 0
            l = r + 1
    
    print(res)

