def merge(lis1, lis2):
    l = 0
    r = 0
    res = []
    while l < len(lis1) and r < len(lis2):
        if lis1[l][0] < lis2[r][0]:
            res.append(lis1[l])
            l += 1
        else:
            res.append(lis2[r])
            r += 1
    
    res.extend(lis1[l:])
    res.extend(lis2[r:])
    return res

def binary(num, lis):
    l = 0
    r = len(lis)

    while l < r:
        mid = (l+r) // 2

        if lis[mid][0] < num:
            l = mid + 1 
        else:
            r = mid
    return r

def mergesort(lis):
    if len(lis[:]) <= 1:
        return lis[:]
    
    mid = len(lis[:])//2
    
    left = mergesort(lis[:mid])
    right = mergesort(lis[mid:])

    left.sort()
    right.sort()

    for i in range(len(left)):
        val = binary(left[i][0], right)

        left[i][0] += val
        a[left[i][1]] += val
    
    for i in range(len(right)):
        val = binary(right[i][0], left)
        right[i][0] += val
        a[right[i][1]] += val
    
    left.sort()
    right.sort()

    return merge(left, right)
    
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    arr = [[num, i] for i, num in enumerate(a)]

    mergesort(arr)

    print(*a)



