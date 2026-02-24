for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    m = 0
    prev = 0
    for num in a:
        m = max(m, num-prev)
        prev = num
    
    m = max(m, (x-prev)*2)
    print(m)