t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    queries = []
    for _ in range(q):
        l, r = map(int, input().split())
        queries.append([l,r])
    summ = []
    for query in queries:
        place = 0
        for i in range(query[0]-1, query[1]-1):
            if i > len(a)-1:
                break
            if i == len(a)-1:
                # place += max(a[i], b[i])
                continue
            aa = max(a[i], a[i+1])
            bb = max(aa, b[i])
            cc = max(bb, b[i+1])
            place += cc
        summ.append(place)
    print(summ)