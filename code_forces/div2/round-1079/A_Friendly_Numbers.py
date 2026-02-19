for _ in range(int(input())):
    x = int(input())
    res = 0
    for i in range(1, 91):
        
        y = x+i
        b = str(y)
        c = sum(int(a) for a in b)
        if c == i:
            res += 1
    print(res)

