k, n, w = map(int, input().split())

tot = 0
for i in range(w):
    tot += (i+1)*k
print(tot-n if tot-n > 0 else 0)