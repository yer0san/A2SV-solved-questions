for _ in range(int(input())):
    n = int(input())
    s = input()

    m = 0
    c = 0
    f = False
    for l in s:
        if l == '#':
            c = 0
        else:
            m += 1
            c += 1
            if c == 3:
                f = True
                break
    if f:
        print(2)
    else:
        print(m)