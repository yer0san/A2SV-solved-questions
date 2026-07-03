def solve():
    a, b = map(int, input().split())
    
    if a == b:
        print('YES')
        print(1)
        print(a)
        return
    
    if b%2 == 0 or b%10 == 1:
        stack = [b]
        while True:
            if b == a:
                print('YES')
                print(len(stack))
                print(*(list(reversed(stack))))
                return
            if b < a:
                break
            if b%2 == 0:
                b //= 2
            elif b%10 == 1:
                b //= 10
            else:
                break
            stack.append(b)

    print('NO')

solve()