n, m = map(int, input().split())
nu = list(map(int, input().split()))
mu = list(map(int, input().split()))

i = 0
j = 0
res = []
while i < len(nu) and j < len(mu):
    if nu[i] <= mu[j]:
        res.append(nu[i])
        i += 1
    else:
        res.append(mu[j])
        j += 1
res += nu[i:]
res += mu[j:]
print(*res)
