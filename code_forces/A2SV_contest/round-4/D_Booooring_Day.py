for _ in range(int(input())):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))

    wn = 0
    res = 0
    left = 0
    for right in range(n):
        wn += a[right]
        while wn > r:
            wn -= a[left]
            left += 1
        if wn >= l and wn <= r:
            res += 1
            wn = 0
            left = right+1

    print(res)


