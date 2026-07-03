# from collections import defaultdict
# from collections import Counter
# from collections import deque
# import bisect
import math

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

def notprime(num, sqn):
    primes = [1, 2, 3, 5, 7]
    if num in primes:
        return False
    
    st = 2
    while st <= sqn:
        if num%st == 0:
            return True
        st += 1
    return False

def solution(_):
    n = ri()
    
    m = 1

    while m < 1000:
        the = ((n*m)+1)
        if notprime(the, math.sqrt(the)):
            print(m)
            return
        m += 1

def main():
    t = 1
    # t = int(ri())
    for _ in range(t):
        solution(_)
 
if __name__ == "__main__":
    main()