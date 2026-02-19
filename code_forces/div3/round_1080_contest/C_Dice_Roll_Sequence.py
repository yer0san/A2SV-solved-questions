for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    i = 0
    res = 0
    while i < n-1:
        if a[i]+a[i+1] == 7 or a[i] == a[i+1]:
            res += 1
            i += 2
            continue
        i += 1
    print(res)