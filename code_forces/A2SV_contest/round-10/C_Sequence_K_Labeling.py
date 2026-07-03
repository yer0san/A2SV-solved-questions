from collections import defaultdict
from collections import Counter
# from collections import deque
# import bisect
# import math

import sys

# sys.setrecursionlimit(10**7) 
# def print(*args, **kwargs):
#     sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))

input = sys.stdin.readline

 
def ri(): return int(input().strip())
def ris(): return map(int, input().split())
def rl(): return list(map(int, input().split()))

# def yn(res): print("YES" if res else "NO")
 
inf = float('inf')
ninf = float('-inf')
# MOD = 10**9 + 7

def solution(_):
    n, k = ris()
    a = rl()
    freq = Counter(a)
    for el in freq:
        if freq[el] > k:
            print('NO')
            return
    
    if len(freq) == n:
        count = 1
        res = []
        while count < k:
            res.append(count)
            count += 1
        added = [k]*(n-(k-1))
        res += added
        print('YES')
        print(*res)
        return
    
    seen = defaultdict(set)
    res = []
    count = 0
    for i in range(n):
        while a[i] in seen[(count%(k))]:
            count += 1

        res.append((count%(k))+1)
        
        seen[(count%(k))].add(a[i])
        count += 1

    print('YES')
    print(*res)

def main():
    t = 1
    # t = int(ri()) 
    for _ in range(t):
        solution(_)
 
if __name__ == "__main__":
    main()
