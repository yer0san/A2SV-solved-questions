# from collections import defaultdict
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
def ris(): return map(int, input().split())
def rl(): return list(map(int, input().split()))

# def yn(res): print("YES" if res else "NO")
 
inf = float('inf')
ninf = float('-inf')
# MOD = 10**9 + 7

def solution(_):
    n, m = ris()
    grid = []
    for _ in range(n):
        l = list(input().strip())
        grid.append(l)
    
    visited = set()
    visiting = set()
    
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    def inbound(r, c, cur):
        if (r < 0 or r >= n or c < 0 or c >= m) or grid[r][c] != cur:
            return False
        return True

    def bfs(r, c):
        cur = grid[r][c]

        q = deque()
        par = [-1, -1]
        q.append((r, c, par))

        while q:
            row, col, parent = q.popleft()
            
            visiting.add((row, col))

            for ar, ac in directions:
                nrow = row+ar
                ncol = col+ac
                if inbound(nrow, ncol, cur):

                    if parent[0] == nrow and parent[1] == ncol:
                        continue

                    if (nrow, ncol) in visiting:
                        return True
                    
                    par = [row, col]
                    q.append((nrow, ncol, par))
            
        for ro, co in visiting:
            visited.add((ro, co))
        
        visiting.clear()
        return False

    for i in range(n):
        for j in range(m):
            if (i, j) not in visited:
                tog = bfs(i,j)
                if tog:
                    print('Yes')
                    return
    print('No')

                  

def main():
    t = 1
    # t = int(ri()) 
    for _ in range(t):
        solution(_)
 
if __name__ == "__main__":
    main()