from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = input()
    freq = Counter(s)
    first = set()
    res = len(freq)
    for l in s:
        first.add(l)
        freq[l] -= 1
        if freq[l] == 0:
            del freq[l]
        res = max(res, len(first)+len(freq))
    print(res)