t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    def countB(a):
        bl = 1
        for i in range(1, len(a)):
            if a[i] != a[i-1]:
                bl += 1
        return bl
    
    bs = 0
    for i in range(n):
        rt = s[i:] + s[:i]
        bs = max(bs, countB(rt))

    print(bs)
