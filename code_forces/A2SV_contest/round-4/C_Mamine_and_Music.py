from collections import defaultdict
def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    mapper = defaultdict(list)
    for i, num in enumerate(a):
        mapper[num].append(i)
    b = sorted(mapper)

    sm = 0
    res = 0
    resl = []

    for num in b:
        for idx in mapper[num]:
            if sm + num > k:
                print(res)
                print(*resl)
                return
            else:
                sm += num
                res += 1
                resl.append(idx+1)
    print(res)
    print(*resl)

solve()