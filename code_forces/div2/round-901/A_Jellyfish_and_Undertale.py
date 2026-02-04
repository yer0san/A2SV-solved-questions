for _ in range(int(input())):
    a, b, n = map(int, input().split())
    res = 0
    tools = list(map(int, input().split()))
    for tool in tools:
        res += min(tool, a)
    print(res+b-1)