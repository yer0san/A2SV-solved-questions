for _ in range(int(input())):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    pre1 = 0
    mx1 = 0
    pre2 = 0
    mx2 = 0
    for num in r:
        pre1 += num
        mx1 = max(mx1, pre1)
    for num in b:
        pre2 += num
        mx2 = max(mx2, pre2)
    print(mx1+mx2)
