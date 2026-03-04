class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        pre_b = [0]*(len(s)+1)
        for st, e, d in shifts:
            if d == 1:
                pre_b[st] += 1
                pre_b[e+1] -= 1
            else:
                pre_b[st] -= 1
                pre_b[e+1] += 1

        pre = [0]
        for pr in pre_b:
            pre.append(pre[-1]+pr)
        off = ord('a')
        for i, l in enumerate(s):
            fir = ord(l)-off
            fir += pre[i+1]
            fir = fir%26
            s[i] = chr(fir+off)
        
        return "".join(s)
