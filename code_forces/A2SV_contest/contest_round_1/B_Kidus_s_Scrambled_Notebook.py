for _ in range(int(input())):
    ab = input()
    found = False
    for i in range(1,len(ab)):
        if ab[i] == "0":
            continue
        a = ab[:i]
        b = ab[i:]
        if int(a) < int(b):
            print(a, b)
            found = True
            break
    if not found:
        print(-1)
