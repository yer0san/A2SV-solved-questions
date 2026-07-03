t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    T_cnt = s.count('T')
    M_cnt = s.count('M')
    if s[0] == 'M' or s[-1] == 'M':
        print('NO')
    elif T_cnt == M_cnt * 2:
        print('YES')
    else:
        print('NO')