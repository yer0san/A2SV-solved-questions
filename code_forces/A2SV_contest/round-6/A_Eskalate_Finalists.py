def solve():
    k = int(input())
    a = list(map(int, input().split()))

    a.sort()
    if a[-1] <= 25:
        print(0)
        return

    st = 1
    res = 0
    i = 0
    size = 0
    while i < k:
        # print(size)
        if a[i] != st:
            st += 1
            size += 1
            continue

        size += 1
        if size > 25:
            res += (size-25)
            size = 25
        i += 1
        st += 1
        
    print(res)
    
solve()