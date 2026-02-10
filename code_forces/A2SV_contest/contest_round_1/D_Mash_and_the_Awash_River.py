for _ in range(int(input())):
    s = input()
    if "**" in s or ">*<" in s or ">*" in s or "*<" in s or "><" in s:
        print(-1)
        continue
    if s == '*':
        print(1)
        continue
    res = 0
    # to right
    for cur in s:
        if cur == '>':
            break
        res += 1

    # to left
    count = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] == '<':
            break
        count += 1
    print(max(res, count))