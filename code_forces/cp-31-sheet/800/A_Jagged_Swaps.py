for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    mn = min(a)
    if a[0] == mn:
        print('YES')
    else:
        print('NO')