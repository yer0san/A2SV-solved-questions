for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a[-1] == max(a):
        a.sort()
        print(a[-1]+a[-2]) 
        continue
    las = a[-1]
    a.sort()
    print(las+a[-1])