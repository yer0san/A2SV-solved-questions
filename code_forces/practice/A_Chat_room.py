s = input()

def find(s):
    hello = "hello"
    idx = 0
    for c in s:
        if c == hello[idx]:
            idx+= 1
        if idx > 4:
            print("YES")
            return
    print("NO")
find(s)
       