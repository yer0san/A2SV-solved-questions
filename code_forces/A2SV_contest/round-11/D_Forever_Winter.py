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
def ris(): return map(int, input().split())
def rl(): return list(map(int, input().split()))

# def yn(res): print("YES" if res else "NO")
 
inf = float('inf')
ninf = float('-inf')
# MOD = 10**9 + 7

def solution(_):
    n, m = ris()
    
    graph = defaultdict(list)
    for _ in range(m):
        u, v = ris()
        graph[u].append(v)
        graph[v].append(u)
    
    prune = defaultdict(int)
    c = -1
    for k in graph:
        if len(graph[k]) == 1:
            c = graph[k][0]
            prune[graph[k][0]] += 1
    
    print(len(prune), prune[c])
        
def main():
    t = 1
    t = int(ri()) 
    for _ in range(t):
        solution(_)
 
if __name__ == "__main__":
    main()