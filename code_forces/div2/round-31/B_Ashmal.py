t = int(input())
for _ in range(t):
    n = int(input())
    strings = list(map(str, input().split()))
    s = strings[0]
    
    for i in range(1, len(strings)):
        if s+strings[i] < strings[i]+s:
            s += strings[i]
        elif s+strings[i] > strings[i]+s:
            s = strings[i]+s
        else:
            s += strings[i]

    print(s)


