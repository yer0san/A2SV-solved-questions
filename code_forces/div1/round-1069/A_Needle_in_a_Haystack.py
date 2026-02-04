for _ in range(int(input())):
    s = input()
    t = list(input())

    holder = []
    seen = set(s)

    for i in range(len(t)):
        if t[i] in seen:
            holder.append(i)
            seen.remove(t[i])
            if not seen:
                break
    if seen:
        print("Impossible")
        continue
    for i in range(len(holder)-1, -1, -1):
        t.pop(holder[i])
    
    t.append(s)
    t.sort()
    print(t)

    # NOT DONE :)

