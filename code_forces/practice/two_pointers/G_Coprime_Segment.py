def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input())
a = list(map(int, input().split()))

if len(a) == 1:
    print(1 if a[0] == 1 else -1)
else:
    wn = gcd(a[0], a[1])
    res = 0
    l = 1
    for r in range(1, n):
        wn = gcd(wn, a[r])
        while wn == 1:
            res += n-r
            wn = gcd(a[l], a[r])
            l += 1
print(res if res != 0 else -1)

