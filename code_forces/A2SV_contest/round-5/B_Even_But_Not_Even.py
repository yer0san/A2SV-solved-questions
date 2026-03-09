for _ in range(int(input())):
    n = int(input())
    s = input()
    lis = [l for l in s]
    odds = {'1', '3', '5', '7', '9'}
    fir = 0
    sec = 0
    found = False
    f = True
    s = False
    for i, num in enumerate(lis):
        if f and num in odds:
            fir = i
            f = False
            s = True
            continue
        if num in odds and s:
            sec = i
            found = True
            break
    if found:
        print(lis[fir]+lis[sec])
    else:
        print(-1)


