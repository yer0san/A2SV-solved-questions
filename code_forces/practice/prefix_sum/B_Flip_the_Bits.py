for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()

    bal = 0
    prefix_bal = [False] * n

    for i in range(n):
        if a[i] == '1':
            bal += 1
        else:
            bal -= 1
        if bal == 0:
            prefix_bal[i] = True

    flipped = False
    pos = True

    for i in reversed(range(n)):
        cur = a[i]
        
        if flipped:
            cur = '1' if cur == '0' else '0'

        if cur != b[i]:
            if not prefix_bal[i]:
                pos = False
                break
            flipped = not flipped

    print("YES" if pos else "NO")