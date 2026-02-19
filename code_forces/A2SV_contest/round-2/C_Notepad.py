from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    s = input()
    done = False
    
    mapper = defaultdict(int)
    for i in range(1, len(s), 2):

        mapper[s[i-1]+s[i]] += 1
        if mapper[s[i-1]+s[i]] >= 2:
            done = True
            break
    if done:
        print('YES')
        continue

    mapper.clear()
    for i in range(2, len(s), 2):
        mapper[s[i-1]+s[i]] += 1
        
        if mapper[s[i-1]+s[i]] >= 2:
            done = True
            break
    if done:
        print('YES')
    else:
        print("NO")







