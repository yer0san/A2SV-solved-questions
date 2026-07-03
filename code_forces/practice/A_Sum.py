t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())

    # a
    if b+c == a:
        print('YES')
    # b
    elif a+c == b:
        print('YES')
    # c
    elif a+b == c:
        print('YES')
    else:
        print('NO')
