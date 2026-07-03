from collections import defaultdict
for _ in range(int(input())):
    n, k = map(int, input().split())
    js = []
    for _ in range(k):
        b, c = map(int, input().split())
        js.append((b, c))
    
    mapp = defaultdict(int)
    js.sort()
    for b, c in js:
        mapp[b] += c
    
    vals = list(mapp.values())
    vals.sort(reverse=True)
    res = 0

    for i in range(n):
        res += vals[i]
        if  i == len(vals)-1:
            break
        
    print(res)