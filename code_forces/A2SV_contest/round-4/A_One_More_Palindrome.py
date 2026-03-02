from collections import Counter
for _ in range(int(input())):
    s = input()
    c = Counter(s)
    f = 0
    found = False
    for l in c:
        if c[l] >= 2:
            f += 1
        if f == 2:
            found = True
            break
    if found:
        print('YES')
    else:
        print('NO')