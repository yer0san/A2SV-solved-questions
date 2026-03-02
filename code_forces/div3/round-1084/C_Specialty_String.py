for _ in range(int(input())):
    n = int(input())
    s = input()

    stack = []

    for i in range(n):
        if not stack or stack[-1] != s[i]:
            stack.append(s[i])
            continue
        if stack[-1] == s[i]:
            stack.pop()
    print('YES' if not stack else 'NO')
