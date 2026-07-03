# greedy

def solve(a):
    n = len(a)
    ans = 0
    maxA = a[-1]
    
    for i in range(2, n):
        k = 0
        
        for j in range(i):
            x = max(maxA, 2 * a[i]) - a[i] - a[j]
            
            while k < j and a[k] <= x:
                k += 1
            
            if k < j:
                ans += j - k
    
    return ans

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))