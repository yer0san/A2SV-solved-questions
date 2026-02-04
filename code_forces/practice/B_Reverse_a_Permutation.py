t = int(input())
for _ in range(t):
    def done():
        n = int(input())
        p = list(map(int, input().split()))
        
        lex = sorted(p, reverse=True)
        for i in range(len(p)):
            if lex[i] != p[i]:
                first = p[:i]
                for j in range(i+1,len(p)):
                    if p[j] > p[i]:
                        last = p[j+1:]
                        mid = p[j:i-1:-1]
                        if i == 0:
                            mid = p[j::-1]

                        p = first + mid + last
                        return p
        return p
    p = done()
    p = [str(n) for n in p]
    print(" ".join(p))
