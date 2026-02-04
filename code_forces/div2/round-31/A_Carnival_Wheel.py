for _ in range(int(input())):
    l, a, b = map(int, input().split())
    seen = set()
    m = 1
    while True:
        num = (a+(m*b))%(l)
        if num in seen:
            break
        seen.add(num)
        m += 1
    print(max(seen))