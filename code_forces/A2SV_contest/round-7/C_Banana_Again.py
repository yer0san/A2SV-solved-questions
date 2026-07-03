n = int(input())
a = list(map(int, input().split()))
ans = [float("inf")]
def helper(ind, g1,g2):
    if ind >= n:
        ans[0] = min(ans[0], abs(sum(g1) - sum(g2)))
        return 
    g1.append(a[ind])
    helper(ind + 1, g1, g2)
    g1.pop()
    g2.append(a[ind])
    helper(ind + 1, g1, g2)
    g2.pop()
helper(0, [], [])
print(ans[0])        


