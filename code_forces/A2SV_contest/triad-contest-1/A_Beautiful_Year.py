yr = int(input())
while True:
    yr += 1
    s = str(yr)
    t = set(s)
    if len(s) == len(t): 
        print(s)
        break