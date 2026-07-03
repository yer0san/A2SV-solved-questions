from collections import defaultdict
s = input()
invs = []
for i, b in enumerate(s):
    if b == ')':
        if invs and s[invs[-1]] == '(':
            invs.pop()
            continue
    invs.append(i)

invs.append(len(s))

mapp = defaultdict(int)

mx = invs[0]
mapp[mx] += 1
for i in range(1, len(invs)):
    sep = (invs[i] - invs[i-1]) - 1
    mx = max(mx, sep)
    mapp[sep] += 1

mapp[0] = 1

print(mx, mapp[mx])


