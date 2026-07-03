for _ in range(int(input())):
    s = input()
    n = len(s)
    
    i = 0
    res = 0
    st = set()
    while i < n:
        if i+1 < n and s[i] == s[i+1]:
            i += 2
            st.clear()
            continue
        
        if i+2 < n:
            if s[i] == s[i+2] or s[i+1] == s[i+2]:
                if s[i+1] == s[i+2] and s[i] in st:
                    res -= 1
                else:
                    res += 1
                i += 3
                st.clear()
                continue

        if s[i] in st:
            res -= 1
            st.clear()
        else:
            res += 1
        st.add(s[i])

        i += 1
        
    print(res)