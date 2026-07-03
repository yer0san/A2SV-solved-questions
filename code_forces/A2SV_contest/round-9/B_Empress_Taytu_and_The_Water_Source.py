for _ in range(int(input())):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    a = list(map(int, input().split()))

    if sum(a) > k:
        print("-1")
        continue

    l = 1
    r = max(d)
    res = r

    while l <= r:
        mid = (l+r) // 2
        tot = 0
        for i in range(n):
            tot += ((d[i]+mid-1)//mid) * a[i]

            if tot > k:
                break
        
        if tot <= k:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    
    print(res)