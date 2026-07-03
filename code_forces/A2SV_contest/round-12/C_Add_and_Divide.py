# from collections import defaultdict
# from collections import Counter
# from collections import deque
# import bisect
import math

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

def rep(a, b):
    res = 0
    while a != 0:
        res += 1
        a //= b
    return res

def solution(_):
    a, b = ris()

    sq = int(math.sqrt(a)) + 1

    cnt = 0
    if b == 1:
        b += 1
        cnt += 1
    
    res = rep(a, b) + cnt

    while b <= sq:
        res = min(res, rep(a, b)+cnt)
        cnt += 1
        b += 1
    print(res)

def main():
    t = 1
    t = int(ri()) 
    for _ in range(t):
        solution(_)
 
if __name__ == "__main__":
    main()