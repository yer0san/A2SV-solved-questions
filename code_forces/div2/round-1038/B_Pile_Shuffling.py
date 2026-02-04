t = int(input())
for _ in range(t):
    n = int(input())
    shortest = 0
    for _ in range(n):
        piles = list(map(int, input().split()))
        
        if piles[0] - piles[2] > 0:
            shortest += piles[0]-piles[2]
        if piles[1]-piles[3] > 0:
            if piles[0]-piles[2] > 0:
                shortest += piles[1]-piles[3] + piles[2]
            else:
                shortest += piles[1]-piles[3] + piles[0]
        
    print(shortest)