a = list(input())
b = list(input())

res = [0, 0]

acntplus = a.count('+')
acntminus = len(a)-acntplus
base = b.count('?')
base = 2**base

def back(st):
    if st > len(a):
        return
    if acntplus == b.count('+') and acntminus == b.count('-'):
        res[1] += 1
        return
    
    for i in range(st, len(a)):
        if b[i] == '?':
            b[i] = '+'
            back(i+1)
            b[i] = '-'
            back(i+1)
            b[i] = '?'

back(0)
res[0] = res[1]/base
        

print(f"{res[0]:.12f}")