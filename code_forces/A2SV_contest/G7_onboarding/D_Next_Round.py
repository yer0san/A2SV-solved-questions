
n, k = map(int, input().split())
scores = list(map(int, input().split()))

res = 0
for score in scores:
    if score >= scores[k-1] and score > 0:
        res += 1
    else:
        break
print(res)
