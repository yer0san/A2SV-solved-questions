def solve(k:int, s:str)->int:
    l = res = 0
    seen = set()
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        if r-l+1 == k:
            res += 1
            seen.remove(s[l])
            l += 1
    return res

k = 5
s = "havefunonleetcode"
print(solve(k, s))
        
        
