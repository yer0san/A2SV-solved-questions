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
    a, b = ris()
    xk, yk = ris()
    xq, yq = ris()
    res = 0

    seen = set()
    find = set()

    seen.add((xk-a, yk-b))
    seen.add((xk+a, yk+b))
    seen.add((xk+a, yk-b))
    seen.add((xk-a, yk+b))
    
    seen.add((xk-b, yk-a))
    seen.add((xk+b, yk+a))
    seen.add((xk+b, yk-a))
    seen.add((xk-b, yk+a))

    find.add((xq-a, yq-b))
    find.add((xq+a, yq+b))
    find.add((xq+a, yq-b))
    find.add((xq-a, yq+b))

    find.add((xq-b, yq-a))
    find.add((xq+b, yq+a))
    find.add((xq+b, yq-a))
    find.add((xq-b, yq+a))

    for i in find:
        if i in seen:
            res += 1
        
    print(res)
        

def main():
    t = 1
    t = int(ri()) 
    for _ in range(t):
        solution(_)
 
if __name__ == "__main__":
    main()