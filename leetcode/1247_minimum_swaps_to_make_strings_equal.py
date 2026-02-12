class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        count1 = Counter(s1)
        count2 = Counter(s2)

        if (count1['x'] + count2['x'])%2 != 0 or (count1['y'] + count2['y'])%2 != 0:
            return -1
        
        s1lis = []
        s2lis = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                s1lis.append(s1[i])
                s2lis.append(s2[i])
        s1 = "".join(s1lis)
        s2 = "".join(s2lis)
        print(s1, s2)

        i = 1
        c1 = 0
        c2 = 0
        while i < len(s1):
            if (s1[i] == 'x' and s1[i-1] == 'y' and s2[i] == 'y' and s2[i-1] == 'x') or (s1[i] == 'y' and s1[i-1] == 'x' and s2[i] == 'x' and s2[i-1] == 'y'):
                c1 += 1
            
            elif (s1[i] == 'x' and s1[i-1] == 'x' and s2[i] == 'y' and s2[i-1] == 'y') or (s1[i] == 'y' and s1[i-1] == 'y' and s2[i] == 'x' and s2[i-1] == 'x'):
                c2 += 1 
            
            i += 2
        
        if c1%2 != 0:
            c1 += 1
        
        return c1 + c2
