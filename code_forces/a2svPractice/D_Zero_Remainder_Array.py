from collections import defaultdict
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    hash = defaultdict(int)
    
    for num in arr:
        if num%k == 0:
            continue
        hash[k-num%k] += 1
        
    key = 0
    val = 0
    if hash:
        for n in arr:
            if hash[k-n%k] > val:
                key = k-n%k
                val = hash[key]
                
            elif hash[k-n%k] == val:
                key = max(key,k-n%k)
                
        print(key+((val-1)*k)+1)
    else:
        print(0)