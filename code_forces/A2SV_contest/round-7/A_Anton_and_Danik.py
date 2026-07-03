n = int(input())
s = input()
ac = 0
dc = 0
for l in s:
    if l == 'A':
        ac += 1
    else:
        dc += 1
if ac > dc:
    print('Anton')
elif dc > ac:
    print('Danik')
else:
    print('Friendship')