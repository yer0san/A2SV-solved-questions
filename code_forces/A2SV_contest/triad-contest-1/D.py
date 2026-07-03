t = int(input())
for _ in range(t):
    s = input()
    a = s.count('1')
    b = len(s)-a

    if a < b:
        print(a)
    elif a > b:
        print(b)
    else:
        print(a-1)
