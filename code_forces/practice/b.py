from collections import Counter
def solve(s:str)->int:
    def S(n:int)->int:
        return (n * (n-1))//2
    
    freq = Counter(s)
    res = 0
    for k in freq:
        res += S(freq[k])
    return len(s) + res

s = "a"
print(solve(s))