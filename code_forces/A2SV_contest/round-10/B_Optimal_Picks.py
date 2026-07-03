# from collections import defaultdict
# from collections import Counter
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

    a.sort(reverse=True)
    eve = 0
    noah = 0
    
    for i in range(n):
        if i%2 == 0:
            eve += a[i]
        else:
            off = a[i]

            if k > 0:
                org = k
                k -= (a[i-1]-a[i])
                if k <= 0:
                    off += org
                else:
                    off += (a[i-1]-a[i])

            noah += off
    
    res = eve-noah

    print(0 if res <= 0 else res)
    
        

def main():
    t = 1
    t = int(ri()) 
    for _ in range(t):
        solution(_)
 
if __name__ == "__main__":
    main()