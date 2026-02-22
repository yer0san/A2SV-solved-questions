n, k = map(int, input().split())
a = input()
c = 0
yes = True
for l in a:
    if l == '.':
        c = 0
    else:
        c += 1
    if c >= k:
        yes = False
        break
if yes:
    print('YES')
else:
    print('NO')