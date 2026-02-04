t = int(input())
for _ in range(t):
    n, s, x = map(int, input().split())
    a = list(map(int, input().split()))
    summ = sum(a)
    if summ < s and (s-summ)%x != 0:
        print("NO")
        continue
    print("YES" if summ <= s else "NO")

