def pfac(n):
    fac = []
    while n % 2 == 0:
        fac.append(2)
        n //= 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            fac.append(i)
            n //= i
        i += 2

    if n > 2:
        fac.append(n)
        
    return fac

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = sorted(a)
    if b == a:
        print('Bob')
        continue

    prms = []
    end = False
    for num in a:
        fac = pfac(num)
        if len(fac) == 0:
            fac.append(1)
            if prms and prms[-1] > fac[0]:
                end = True
                break
            prms.append(fac[0])
            continue

        if len(fac) == 1: 
            if prms and prms[-1] > fac[0]:
                end = True
                break
            prms.append(fac[0])
            continue
        
        if fac[0] < fac[-1]:
            end = True
            break
        prms.extend(fac)

    if end:
        print('Alice')
        continue
    
    if sorted(prms) == prms:
        print('Bob')
    else:
        print('Alice')



