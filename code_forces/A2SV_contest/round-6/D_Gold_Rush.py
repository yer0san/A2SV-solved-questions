def divi(n, m):
    if n == m:
        return True
    if n < m or n%3 != 0:
        return False
    f = n//3
    g = f*2
    ans = divi(f, m) or divi(g, m)
    return ans

for _ in range(int(input())):
    n, m = map(int, input().split())
    print('YES' if divi(n, m) else 'NO')
