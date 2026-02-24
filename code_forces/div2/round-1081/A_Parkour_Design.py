for _ in range(int(input())):
    x, y = map(int, input().split())

    if y > 0:
        x -= y*2
    elif y < 0:
        x -= abs(y)*4
    
    if x < 0 or x%3 != 0:
        print('NO')
    else:
        print('YES')
    