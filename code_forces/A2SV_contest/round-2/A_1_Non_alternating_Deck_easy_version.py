for _ in range(int(input())):
    n = int(input())
    # this is an up-solve solution, u can get the original on codeforces submissions

    bobcount = 3
    alicecount = 1

    bob = 0

    # first, for bob
    prev1 = 0
    summ = (bobcount*(bobcount+1))//2
    while summ <= n:
        bob += (2*bobcount)-1
        bobcount += 4
        prev1 = summ
        summ = (bobcount*(bobcount+1))//2

    alice = 0
    
    # for alice
    prev2 = 0
    summ2 = (alicecount*(alicecount+1))//2
    while summ2 <= n:
        alice += (2*alicecount)-1
        alicecount += 4
        prev2 = summ2
        summ2 = (alicecount*(alicecount+1))//2
    
    # calculate for leftovers
    # first find the furthest from summ and summ2 to the given n

    if alicecount < bobcount:
        alice += (n-prev1)
    else:
        bob += (n-prev2)

    print(alice, bob)

