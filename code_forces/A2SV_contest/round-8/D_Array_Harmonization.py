for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.append(1)
    a.sort(reverse=True)
    b.sort(reverse=True)
    l = 0
    
    res = 0

    for i in range(n):
        if a[i] >= b[l]:
            res += 1
            continue
        l += 1

    print(res)
