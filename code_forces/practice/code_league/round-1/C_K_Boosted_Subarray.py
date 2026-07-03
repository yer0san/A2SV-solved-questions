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

def trier(arr):
    val = True

    for num in arr:
        if num > 0:
            val = False
            break
    if val:
        return max(arr)
    
    ans = arr[0]
    wn = 0

    for num in arr:
        wn += num
        if wn < 0:
            wn = 0
        ans = max(wn, ans)
    
    return ans

def solution(_):
    n, k = ris()
    a = rl()

    cur = []

    for num in a:
        cur.append(num*k)
    
    mx = trier(cur)

    cur = []
    for num in a:
        cur.append(num//k)
    
    mx = max(mx, trier(cur))

    print(mx)
     

def main():
    t = 1
    t = int(ri()) 
    for _ in range(t):
        solution(_)
 
if __name__ == "__main__":
    main()