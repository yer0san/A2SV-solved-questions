def solve():
    n, m = map(int, input().split())
    a = 0
    diff = []
    for _ in range(n):
        x, y = map(int, input().split())
        a += x
        diff.append(x-y)
    
    if a <= m:
        print(0)
        return
    
    diff.sort(reverse=True)
    res = 0
    for d in diff:
        a -= d
        res += 1
        if a <= m:
            print(res)
            return
    print(-1)

solve()
    

       

    