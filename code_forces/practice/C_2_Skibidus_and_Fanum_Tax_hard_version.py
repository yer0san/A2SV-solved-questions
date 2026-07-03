from bisect import bisect_left

def mapper():
    return map(int, input().split())

for _ in range(int(input())):
    n, m = mapper()
    a = list(mapper())
    b = list(mapper())

    b.sort()
    no = False
    prev = float('-inf')
    
    for num in a:
        c = float('inf')
        if num >= prev:
            c = min(c, num)
        numm = prev + num

        i = bisect_left(b, numm)

        if i < m:
            ch = b[i] - num
            if ch >= prev:
                c = min(c, ch)

        if c == float('inf'):
            no = True
            break
        prev = c

    print('NO' if no else 'YES')
