for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    for i in range(0, len(a), 2):
        h = []
        j = i+1
        while j <= n:
            h.append(a[j-1])
            j *= 2
        
        h.sort()

        j = i+1
        c = 0
        while j <= n:
            a[j-1] = h[c]
            j *= 2
            c += 1
        
    count = 1
    no = False
    for num in a:
        if num != count:
            no = True
            break
        count += 1
    print("NO" if no else "YES")