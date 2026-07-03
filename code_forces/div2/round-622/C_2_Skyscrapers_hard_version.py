n = int(input())
m = list(map(int, input().split()))

def prefix(lis):
    res = [lis[0]]
    stack = [(lis[0],1)]

    for i in range(1, len(lis)):
        count = 1
        subt = 0
        while stack and stack[-1][0] > lis[i]:
            l, ct = stack.pop()
            count += ct
            subt += l*ct

        stack.append((lis[i], count))
        res.append(res[-1]-subt+(lis[i]*count))
    return res

pre = prefix(m)

suff = list(reversed(prefix(list(reversed(m)))))

mx = (0, 0)
for i, num in enumerate(pre):
    if mx[0] < (num+suff[i]-m[i]):
        mx = (num+suff[i]-m[i], i)

res = [0]*len(m)
idx = mx[1]
mn = m[idx]

# to the left
for i in range(idx, -1, -1):
    mn = min(mn, m[i])
    res[i] = mn

# to the right
mn = m[idx]
for i in range(idx, len(m)):
    mn = min(mn, m[i])
    res[i] = mn
print(*res)


