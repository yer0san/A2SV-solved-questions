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
    n = ri()
    ax, ay = ris()
    bx, by = ris()
    cx, cy = ris()

    if bx < ax and cx > ax:
        print('NO')
        return
    if bx > ax and cx < ax:
        print('NO')
        return
    
    if by > ay and cy < ay:
        print('NO')
        return
    if by < ay and cy > ay:
        print('NO')
        return
    print('YES')
        

def main():
    t = 1
    # t = int(ri()) 
    for _ in range(t):
        solution(_)
 
if __name__ == "__main__":
    main()