# from collections import Counter
# for _ in range(int(input())):
#     n, l, r = map(int, input().split())
#     socks = list(map(int, input().split()))
    
#     res = 0
#     if l != r:
#         if l < r:
#             one = socks[:l]
#             tw = socks[l:]
#         if l > r:
#             one = socks[l:]
#             tw = socks[:l]

#         cntOne = Counter(one)
#         c = abs(l-r)//2
#         res += c
        
#         idx = 0
#         d = set()
#         while c > 0:
#             if cntOne[tw[idx]] == 0:
#                 c -= 1
#                 one.append(tw[idx])
#                 cntOne[tw[idx]] += 1
#                 d.add(idx)
#                 idx += 1
#                 continue
#             cntOne[tw[idx]] -= 1
#             idx += 1
#         two = []
#         for i, num in enumerate(tw):
#             if i not in d:
#                 two.append(num)
        
#     else:
#         one = socks[:l]
#         two = socks[l:]
    
#     cntOne = Counter(one)
#     cntTwo = Counter(two)

#     for charr in cntOne:
#         if cntOne[charr] > cntTwo[charr]:
#             res += cntOne[charr]-cntTwo[charr]
    
#     print(res) This was my approach, I couldn't do it :)

for _ in range(int(input())):
    N, L, R = map(int, input().split())
    C = list(map(int, input().split()))
    
    lcnt = [0] * (N + 1)
    rcnt = [0] * (N + 1)

    # Count left and right socks
    for i in range(N):
        if i < L:
            lcnt[C[i]] += 1
        else:
            rcnt[C[i]] += 1

    # Remove already matching pairs
    for i in range(1, N + 1):
        mn = min(lcnt[i], rcnt[i])
        lcnt[i] -= mn
        rcnt[i] -= mn
        L -= mn
        R -= mn

    # Ensure L >= R
    if L < R:
        lcnt, rcnt = rcnt, lcnt
        L, R = R, L

    ans = 0

    # Convert extra pairs on heavier side
    for i in range(1, N + 1):
        extra = L - R  # always even
        canDo = lcnt[i] // 2
        Do = min(canDo * 2, extra)

        ans += Do // 2
        L -= Do

    # Final adjustments
    ans += (L - R) // 2 + (L + R) // 2

    print(ans) # editorial approach


        
        

    
    
    

    