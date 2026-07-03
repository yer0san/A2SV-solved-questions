for _ in range(int(input())):
    n, m = map(int, input().split())
    s = input()
    w = input()

    sm1 = 0
    for l in w:
        sm1 += ord(l)
    
    wn = 0
    l = 0
    found = False
    for i in range(n):
        wn += ord(s[i])
        if i-l+1 == m:
            if sm1 == wn:
                found = True
                break
            wn -= ord(s[l])
            l += 1
    if found:
        print('YES')
    else:
        print('NO')