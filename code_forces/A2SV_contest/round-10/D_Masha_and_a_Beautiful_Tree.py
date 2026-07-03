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
    m = ri()
    p = rl()
    no = [False]
    res = [0]

    def recur(arr):
        if len(arr) == 1 or no[0]:  
            return arr
        
        l = 0
        r = len(arr)

        mid = l + ((r-l)//2)
        left = recur(arr[:mid])
        right = recur(arr[mid:])

        mxl = max(left)
        mnl = min(left)
        mxr = max(right)
        mnr = min(right)
    
        if (mnl > mxr):
            res[0] += 1
        else:
            if mxl > mnr:
                no[0] = True
        
        return left+right

    recur(p)

    if no[0]:
        print(-1)
    else:
        print(res[0])
        

def main():
    t = 1
    t = int(ri()) 
    for _ in range(t):
        solution(_)
 
if __name__ == "__main__":
    main()