t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
        continue
    if n == 2:
        print(9)
        continue
    one = (n**2) + ((n**2)-1) + (n**2)-2 + (n*(n-1))-1
    two = ((n**2)-1) + ((n*(n-1))-1) + (n*(n-1))-2 + (n*(n-1)) + (n*(n-2)-1)
    print(max(one, two))