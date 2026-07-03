for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    st = set(arr)

    if len(st) > 1 or len(arr) == 1: 
        print(-1)
        continue
    
    res = [n]

    for i in range(1, n):
        res.append(i)

    print(*res)
