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
    n, m = ris()

    las = True
    for i in range(n):
        if i&1:
            if las:
                las = False
                s = '.'*(m-1)
                s += '#'
                print(s)
            else:
                las = True
                s = '#'
                s += '.'*(m-1)
                print(s)
        else:
            print('#'*m)
        

def main():
    t = 1
    # t = int(ri()) 
    for _ in range(t):
        solution(_)
 
if __name__ == "__main__":
    main()