for _ in range(int(input())):
    n = int(input())
    s = input()
    
    if n%2 == 0:
        mid = (n-1)//2
        c = s[mid]
        res = 0
        
        while mid >= 0 and s[mid] == c:
            res += 1
            mid -= 1
        print(res*2)
    else:
        mid = (n-1)//2
        c = s[mid]
        res = 0
        mid -= 1
        while mid >= 0 and s[mid] == c:
            res += 1
            mid -= 1
        print((res*2)+1)