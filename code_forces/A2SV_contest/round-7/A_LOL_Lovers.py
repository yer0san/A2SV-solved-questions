from collections import Counter
n = int(input())
s = input()

freq = Counter(s)

if freq[s[0]] == 2:
    cur = s[0]
    if cur == 'L':
        noncur = 'O'
    else:
        noncur = 'L'

    curc = 0
    noncurc = 0

    for i, l in enumerate(s):
        if l == cur:
            curc += 1
            if i == n-1:
                print(-1)
                break
            if i == n-1 or (curc == 2 and noncurc == freq[noncur]-noncurc):
                print(-1)
                break
            
            if curc == 2:
                print(i+1)
                break
        else:
            noncurc += 1
else:
    print(1)

