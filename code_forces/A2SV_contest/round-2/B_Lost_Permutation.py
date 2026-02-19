for _ in range(int(input())):
    m, s = map(int, input().split())
    found = list(map(int, input().split()))

    found.sort()
    summ = sum(found)
    last = found[-1]
    adder = 2

    full_sum = ((last+1)*last)//2

    while full_sum - summ < s:
        full_sum = ((last+adder)*(last+adder-1))//2
        adder += 1

    if full_sum - summ == s:
        print("YES")
        continue
    print('NO')