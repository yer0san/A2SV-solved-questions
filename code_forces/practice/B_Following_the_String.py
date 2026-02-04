from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    letter_map = defaultdict(list)
    letter_map[0] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                      'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                        'w', 'x', 'y', 'z']
    res =  []
    for num in a:
        c = letter_map[num][-1]
        res.append(c)
        letter_map[num+1].append(c)
        letter_map[num].pop()
    print("".join(res))
