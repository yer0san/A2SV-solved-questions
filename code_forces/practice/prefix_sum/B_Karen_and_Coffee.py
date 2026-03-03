n, k, q = map(int, input().split())
mn = float('inf')
mx = 0
recipes = []
for _ in range(n):
    l, r = map(int, input().split())
    mn = min(mn, l)
    mx = max(mx, r)
    recipes.append([l, r])

pre = [0]*(mx-mn+2)
for l, r in recipes:
    idx1 = l - mn
    idx2 = r - mn + 1
    pre[idx1] += 1
    pre[idx2] -= 1

pre2 = [0]
for i in range(len(pre)-1):
    pre2.append(pre2[-1]+pre[i])

prefix_sum = [0]
for p in pre2[1:]:

    if p >= k:
        prefix_sum.append(prefix_sum[-1]+1)
    else:
        prefix_sum.append(prefix_sum[-1])

for _ in range(q):
    a, b = map(int, input().split())
    if a > mx or b < mn:
        print(0)
        continue
    idx1 = a-mn
    if a < mn:
        idx1 = mn-mn
    idx2 = b-mn+1
    if b > mx:
        idx2 = mx-mn+1
    print(prefix_sum[idx2]-prefix_sum[idx1])
