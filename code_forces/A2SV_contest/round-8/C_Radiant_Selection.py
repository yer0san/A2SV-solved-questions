import math
for _ in range(int(input())):
    k = int(input())

    l = k
    r = k*2

    while l < r:
        mid = l+(r-l)//2
        
        perf = math.isqrt(mid)
        val = mid - perf

        if val == k:
            r = mid
        if val > k:
            r = mid - 1
        if val < k:
            l = mid + 1

    print(r)