for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    c = 0

    for k in range(2,n):
        tmp = max(a[k], a[-1] - a[k])
        l , r = 0 , k -1
        while l < r :
            if a[l] + a[r] > tmp :
                c += (r - l)
                r -= 1
            else:
                l += 1

    print(c)