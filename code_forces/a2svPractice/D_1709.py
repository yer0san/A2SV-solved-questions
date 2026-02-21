for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    k = 0
    lis = []
    # bubble sort a and b
    for i in range(len(a)):
        for j in range(1, len(a)):
            if a[j] < a[j-1]:
                k += 1
                lis.append([1, j])
                a[j-1], a[j] = a[j], a[j-1]
    
    for i in range(len(b)):
        for j in range(1, len(b)):
            if b[j] < b[j-1]:
                k += 1
                lis.append([2, j])
                b[j-1], b[j] = b[j], b[j-1]
    
    for i in range(len(a)):
        if a[i] > b[i]:
            k += 1
            lis.append([3, i+1])
    
    print(k)
    for num, idx in lis:
        print(num, idx)
    