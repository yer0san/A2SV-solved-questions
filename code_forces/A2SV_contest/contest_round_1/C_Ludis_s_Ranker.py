n = int(input())
ratings = list(map(int, input().split()))
ranks = sorted(ratings, reverse=True)
mapper = {}
prev = 0
for i in range(len(ranks)):
    if ranks[i] == prev:
        mapper[ranks[i]] = mapper[prev]
    else:
        mapper[ranks[i]] = i+1
    prev = ranks[i]
res = []
for rating in ratings:
    res.append(str(mapper[rating]))

print(" ".join(res))