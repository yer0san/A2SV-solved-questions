t = int(input())
for _ in range(t):
    s = input()
    q = int(input())
    queries = list(map(int, input().split()))

    n = len(s)
    res = []
    for query in queries:
        flip = 0
        while query > n:
            m = n
            while query > m:
                m *= 2
            m //= 2
            if query > m:
                query -= m
                flip = 1-flip
        l = s[query-1]

        if flip:
            if l.isupper():
                l = l.lower()
            else:
                l = l.upper()
        res.append(l)
    print(*res)
