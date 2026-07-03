for _ in range(int(input())):
    n, h = map(int, input().split())

    mx = 0
    for _ in range(n):
        hi, w = map(int, input().split())
        mx += max(hi, w)
    print('YES' if mx >= h else 'NO')