def solve():
    n = int(input())
    s = input()
    st = set(s)
    if n > 1 and len(s) == len(st):
        print('No')
    else:
        print('Yes')

solve()