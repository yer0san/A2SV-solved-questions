for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    s = sorted(a)
    if a == s:
        print('YES')
        continue
    if k < 2:
        print('NO')
    else:
        print('YES')