t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if n == 1 or m == 1:
        print("NO")
        continue
    if n < 3 and m < 3:
        print("NO")
    else:
        print("YES")