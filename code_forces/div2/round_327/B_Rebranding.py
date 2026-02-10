from collections import defaultdict
n, m = map(int, input().split())
name = input()

holder = defaultdict(list)
# populate
for i,l in enumerate(name):
    holder[l].append(i)

for _ in range(m):
    x, y = map(str, input().split())
    holder[x], holder[y] = holder[y], holder[x]

res = ["" for _ in range(len(name))]
for key in holder:
    for idx in holder[key]:
        res[idx] = key
print("".join(res))