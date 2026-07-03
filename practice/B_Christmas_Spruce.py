from collections import defaultdict
n = int(input())
mapp = defaultdict(int)
for _ in range(n-1):
    i = int(input())
    mapp[i] += 1

diff = 3
yes = True
for num in list(reversed(mapp.keys())):
    if mapp[num] < diff:
        yes = False
        break
    diff += 1
print('Yes' if yes else 'No')