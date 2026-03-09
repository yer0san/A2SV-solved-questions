from collections import defaultdict, Counter
for _ in range(int(input())):
    w = input()
    p = int(input())

    off = ord('a')-1
    freq = Counter(w)
    mapper = []
    tot = 0
    for i,l in enumerate(w):
        mapper.append([l, ord(l)-off])
        tot += ord(l)-off
    if tot <= p:
        print(w)
        continue
    
    b = sorted(mapper, key=lambda x:x[1], reverse=True)
    for l, idx in b:
        tot -= idx
        freq[l] -= 1
        if freq[l] == 0:
            del freq[l]
        if tot <= p:
            break
        
    res = []
    for l in w:
        if l in freq:
            res.append(l)
            freq[l] -= 1
            if freq[l] == 0:
                del freq[l]
    print("".join(res))




