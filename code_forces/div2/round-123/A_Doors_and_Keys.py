for _ in range(int(input())):
    mapp = input()
    capitals = set()
    no = False
    for letter in mapp:
        if ord(letter) > 97 and letter.upper() in capitals:
            print("NO")
            no = True
            break
        if ord(letter) < 97:
            capitals.add(letter)
    if not no:
        print("YES")

        
