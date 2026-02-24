for _ in range(int(input())):
    s = input()

    res = set()

    l = 0
    while l < len(s):
        if l+1 == len(s):
            res.add(s[l])
            l += 1
            continue
        if s[l] != s[l+1]:
            res.add(s[l])
            l += 1
            continue
        l += 2
    ress = sorted(res)
    print("".join(ress))
        