n = int(input())
a = list(map(int, input().split()))

s = sum(a)
tot = (n*(n+1))//2
print(tot-s)