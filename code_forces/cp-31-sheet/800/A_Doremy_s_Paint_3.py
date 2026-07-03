from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    freq = Counter(a)
    if len(freq) == 1:
        print('Yes')
    
    elif len(freq) > 2:
        print('No')
    else:
        ct1, ct2 = freq.keys()
        if abs(freq[ct1] - freq[ct2]) > 1:
            print('No')
        else:
            print('Yes')
