from collections import defaultdict
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

def solution(_):
    n, m = ris()
    
    grid = defaultdict(set)
    
    for _ in range(m):
        i, j = ris()
        grid[i].add(j)
        grid[j].add(i)

    res = 0
    leaf = True

    while leaf:
        leaf = False
        leafs = []

        for k in grid:
            if len(grid[k]) == 1:
                leaf = True
                leafs.append(k)

        for k in leafs:
            num = -1
            for i in grid[k]:
                num = i
            grid[k] = set()
    
            if num != -1 and grid[num]:
                grid[num].remove(k)

        if leaf:
            res += 1

    print(res)
        

def main():
    t = 1
    # t = int(ri()) 
    for _ in range(t):
        solution(_)
 
if __name__ == "__main__":
    main()