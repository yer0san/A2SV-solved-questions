for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    res = [a[0]]

    for i in range(1, n - 1):
        prev = a[i] - a[i - 1]
        nxt = a[i + 1] - a[i]

        if prev * nxt < 0:
            res.append(a[i])

    res.append(a[-1])

    print(len(res))
    print(*res)