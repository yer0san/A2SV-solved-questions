for _ in range(int(input())):
    n = int(input())
    n -= 1
    res = [1, 0, 0, 0]
    p = 1
    od = 2

    while n:
        val = (2*od)+1
        added = min(val, n)

        if p:
            if added%2 == 0:
                res[p+1] += added//2
                res[p+2] += added//2
            else:
                res[p+1] += added//2
                res[p+2] += (added//2)+1
        else:
            if added%2 == 0:
                res[p+1] += added//2
                res[p] += added//2
            else:
                res[p+1] += added//2
                res[p] += (added//2)+1
        
        p = 1-p
        n -= min(n, added)
        od += 2

    print(*res)

