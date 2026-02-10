for _ in range(int(input())):
    n = int(input())
    s = input()
    if "aa" in s:
        print(2)
        continue
    elif "aba" in s or "aca" in s:
        print(3)
        continue
    elif "abca" in s or "acba" in s:
        print(4)
        continue
    elif "abbacca" in s or "accabba" in s:
        print(7)
        continue
    print(-1)