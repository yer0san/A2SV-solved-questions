for _ in range(int(input())):
    n, m = map(int, input().split())

    grid1 = []
    for _ in range(n):
        hold = list(map(int, input().split()))
        grid1.append(hold)

    if n == 1 and m == 1:
        print(-1)
        continue
    
    for i in range(n):
        nw = grid1[i][0]
        for j in range(m-1):
            grid1[i][j] = grid1[i][j+1]
        grid1[i][-1] = nw
    
    nw = grid1[0][::]
    for i in range(n-1):
        grid1[i] = grid1[i+1][::]
    
    grid1[-1] = nw[::]
    for i in range(n):
        print(*grid1[i])

