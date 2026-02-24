from collections import Counter
for _ in range(int(input())):
    s = list(input())
    t = input()

    freq_s = Counter(s)
    freq_t = Counter(t)
    
    big = 'a'
    for w in freq_s:
        if freq_s[w] > freq_t[w]:
            print('Impossible')
            break
    else:
        new = []
        p = 0
        for w in t:
            if w not in freq_s:
                new.append(w)
                
            else:
                freq_s[w] -= 1
                if freq_s[w] == 0:
                    del freq_s[w]
        
        new.sort()

        res = []
        p = 0
        i = 0
        while i < len(s):
            while p < len(new) and s[i] > new[p]:
                res.append(new[p])
                p += 1
            res.append(s[i])
            i += 1
                
        res.extend(new[p:])
        print("".join(res))

            
        
            


            



        




    

