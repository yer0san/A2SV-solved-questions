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

def rs(): return input().strip()

def rsl(): return list(input().strip())

def ris(): return map(int, input().split())

def rl(): return list(map(int, input().split()))

# def yn(res): print("YES" if res else "NO")
 
inf = float('inf')
ninf = float('-inf')
# MOD = 10**9 + 7

def solution(_):
    r1, c1, r2, c2 = ris()
    res = [0, 0, 0]

    # for rook
    rf = False
    if r1 == r2:
        res[0] = 1
        rf = True
    if c1 == c2:
        res[0] = 1
        rf = True
    
    if not rf:
        res[0] = 2
    
    # for bishop
    # check same color
    bf = False
    if (r1+c1)&1 and (r2+c2)&1:
        bf = True

        if ((r1-c1) == (r2-c2)) or ((r1+c1) == (r2+c2)):
            res[1] = 1

        else:
            res[1] = 2
            
        
    if (r1+c1) % 2 == 0 and (r2+c2) % 2 == 0:
        bf = True

        if (r1-c1) == (r2-c2) or (r1+c1) == (r2+c2):
            res[1] = 1
        else:
            res[1] = 2
    
    if not bf:
        res[1] = 0

    # for the king
    kf = False
    if r1 == r2:
        kf = True
        res[2] = abs(c1-c2)
    if c1 == c2:
        kf = True
        res[2] = abs(r1-r2)
    
    # same diagonal
    if not kf:
        if (r1-c1) == (r2-c2) or (r1+c1) == (r2+c2):
            kf = True
            res[2] = abs(r1-r2)

    # shortest path for the king, fuck
    shor = [inf]
    if not kf:
        def inbound(r, c):
            if r < 1 or r > 8 or c < 1 or c > 8:
                return False
            
            return True
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        vis = set()
        
        def bfs(r1, c1, r2, c2):
            q = deque()
            q.append((r1, c1, 0))
            vis.add((r1, c1))
        
            while q:
                r, c, cnt = q.popleft()

                if r == r2 and c == c2:
                    shor[0] = min(shor[0], cnt)
                
                for i, j in directions:
                    nr, nc = r+i, c+j

                    if (nr, nc) in vis:
                        continue

                    if inbound(nr, nc):
                        vis.add((nr, nc))
                        q.append((nr, nc, cnt+1))

        bfs(r1, c1, r2, c2)

        res[2] = shor[0]
        
    print(*res)

  

def main():
    t = 1
    # t = int(ri()) 
    for _ in range(t):
        solution(_)
 
if __name__ == "__main__":
    main()