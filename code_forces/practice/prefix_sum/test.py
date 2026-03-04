from collections import defaultdict
k = int(input())
a = list(map(int, input().split()))

pre = 0
mapper = defaultdict(int)
mapper[0] = 1
res = 0

for num in a:
    pre += num

    if pre%k in mapper:
        res += mapper[pre%k]

    mapper[pre%k] += 1

print(res)
