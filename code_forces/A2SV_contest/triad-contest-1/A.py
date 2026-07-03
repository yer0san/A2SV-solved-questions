for _ in range(int(input())):
    d, t = map(int, input().split())
    t = float(t)
    d = float(d)
    res = 0
    while d > t:
        d /= 2
        res += 1
    print(res)
