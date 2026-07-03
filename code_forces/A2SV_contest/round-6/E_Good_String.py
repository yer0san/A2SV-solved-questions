n = int(input())
s = input()

res = []
i = 0
while i < n-1:
    if s[i] !=  s[i+1]:
        res.append(s[i])
        res.append(s[i+1])
        i += 2
        continue
    i += 1

l = n-len(res)
print(l)
print("".join(res))