t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    maxx = a[-1]
    count = 0
    for i in range(len(a)-1, -1, -1):
        l = 0
        r = i-1     
        while l<r:
            if a[l] +a[r] > a[i] and a[i] + a[l] + a[r] > maxx:
                count += (r-l)
                r -=1
            else:
                l += 1

    print(count)  