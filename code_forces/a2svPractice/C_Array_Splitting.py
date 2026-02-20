n, k = map(int, input().split())
a = list(map(int, input().split()))

diff = []
for i in range(1, n):
    diff.append(a[i]-a[i-1])

diff.sort()

print(sum(diff[:(len(diff)-k+1)]))

