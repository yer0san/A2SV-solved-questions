for _ in range(int(input())):
    n, k = map(int, input().split())
    casinos = []
    for _ in range(n):
        lis = list(map(int, input().split()))
        casinos.append(lis)
    
    casinos.sort()
    m = 0
    for casino in casinos:
        if casino[0] > k or casino[1] < k:
            k = max(k, m)
        if casino[0] <= k and casino[1] >= k:
            m = max(m, casino[2])
            
    print(max(m, k))
        

