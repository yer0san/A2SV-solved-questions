for _ in range(int(input())):
    n= int(input())
    a = list(map(int, input().split()))
    pre = [0]
    res = 0

    for i, num in enumerate(a):
        if num >= i+1:
            pre.append(pre[-1])
            continue
        pre.append(pre[-1]+1)

        if num == 0:
            continue

        res += pre[num-1]

    print(res)
