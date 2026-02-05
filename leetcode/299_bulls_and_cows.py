class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        rep = Counter(secret)
        a = 0
        b = 0
        idxs = []
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                rep[guess[i]] -= 1
                a += 1
            else:
                idxs.append(i)
        
        for idx in idxs:
            if rep[guess[idx]] > 0:
                rep[guess[idx]] -= 1
                b += 1
            

        return f"{a}A{b}B"
