t = int(input())
def done(t):
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        s = sum(b)
        count = b.count(0)
        non = len(b)-count

        if s > len(b):
            while s - non < len(b)-1:
                non -= 1
            print(non)
            continue

        print(1)
done(t)
