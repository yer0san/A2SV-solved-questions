from collections import defaultdict
# from collections import Counter
from collections import deque
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

def minDist(dest, st, mn, grid):
    q = deque()
    visited = set()
    q.append((st, 0))

    while q:
        cur, c = q.popleft()
        if cur == dest:
            return c
        
        if c >= mn:
            return mn
        
        visited.add(cur)
        for nbr in grid[cur]:
            if nbr in visited:
                continue

            q.append((nbr, c+1))
        

def solution(_):
    w = rs()
    n, k = ris()
    fr = rl()

    grid = defaultdict(list)

    for _ in range(n-1):
        i, j = ris()
        grid[i].append(j)
        grid[j].append(i)
    
    leafs = []
    for i in grid:
        if len(grid[i]) == 1:
            leafs.append(i)
    
    mindist = defaultdict(int)
    for l in leafs:
        mindist[l] = inf
    
    for l in leafs:
        for f in fr:
            mindist[l] = minDist(l, f, mindist[l], grid)
    
    for l in leafs:
        if l == 1:
            continue
        min1 = minDist(l, 1, inf, grid)
        # print(n, k)
        # print(l)
        # print(min1, mindist[l])
        if min1 < mindist[l]:
            print('YES')
            return
        
    print('NO')

    

def main():
    t = 1
    t = int(ri()) 
    for _ in range(t):
        solution(_)
 
if __name__ == "__main__":
    main()