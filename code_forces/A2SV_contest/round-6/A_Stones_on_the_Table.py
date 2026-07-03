# not in the contest
def solve():
    n = int(input())
    s = input()
    if n == 1:
        print(0)
        return
    res = 0
    for i in range(1, n):
        if s[i] == s[i-1]:
            res += 1
    print(res)


solve()