n = int(input())
prev = input()

grps = 1

for _ in range(n - 1):
    cur = input()
    if cur != prev:
        grps += 1
    prev = cur

print(grps)