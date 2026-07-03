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

def rs(): return input().strip()

def rsl(): return list(input().strip())

def ris(): return map(int, input().split())

def rl(): return list(map(int, input().split()))

# def yn(res): print("YES" if res else "NO")
 
inf = float('inf')
ninf = float('-inf')
# MOD = 10**9 + 7

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solution(_):
    n = ri()
    l = rl()
    c = rl()

    mn = inf
    for i in range(n):
        mn = min(mn, l[i]*c[i])
    
    gc = l[0]
    lcm = gc
    for i in range(1, n):
        gc = gcd(lcm, l[i])
        lcm = (lcm * l[i])//gc

    if lcm > mn:
        print(-1)
        return
    print(lcm)
    res = []
    for num in l:
        res.append(lcm//num)
    print(*res)   

def main():
    t = 1
    t = int(ri()) 
    for _ in range(t):
        solution(_)
 
if __name__ == "__main__":
    main()