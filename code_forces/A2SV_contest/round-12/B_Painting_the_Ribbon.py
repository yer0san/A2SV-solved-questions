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
    n, m, k = ris()
    c = 0

    freq = defaultdict(int)

    for i in range(n):
        freq[i%m] += 1
    mx = 0
    for num in freq:
        mx = max(mx, freq[num])
    
    print('YES' if (n-mx) > k else 'NO')

def main():
    t = 1
    t = int(ri()) 
    for _ in range(t):
        solution(_)
 
if __name__ == "__main__":
    main()