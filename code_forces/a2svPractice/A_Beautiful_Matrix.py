row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))
row4 = list(map(int, input().split()))
row5 = list(map(int, input().split()))

r = 0
c = 0
for i in range(len(row1)):
    if row1[i] == 1:
        r, c = 0, i
        break
    elif row2[i] == 1:
        r, c = 1, i
        break
    elif row3[i] == 1:
        r, c = 2, i
        break
    elif row4[i] == 1:
        r, c = 3, i
        break
    elif row5[i] == 1:
        r, c = 4, i
        break
print(abs(2-r)+abs(2-c))