from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    freq = Counter(arr)
    res = 0
    for st in freq:
        if freq[st] >= 3:
            res += freq[st]//3
    print(res)