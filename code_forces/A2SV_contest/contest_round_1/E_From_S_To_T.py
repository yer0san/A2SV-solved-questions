q= int(input())
for _ in range(q):
    s = input()
    t = input()
    p = input()
    temp = list(p)
    s_count = 0
    ans = "YES"
    if len(t) == 0 and len(s) != 0:
        ans = "NO"
    for i in range(len(t)):
        if s_count < len(s) and t[i] == s[s_count]:
            s_count += 1
        elif t[i] in temp:
            temp.remove(t[i])
        else:
            ans = "NO"
            break
    if s_count != len(s):
        ans = "NO"     
    print(ans)
