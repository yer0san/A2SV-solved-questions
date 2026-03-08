class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        st = set()
        for num in nums:
            st.add(int(num, 2))
        
        n = 0
        res = ""
        while True:
            if n not in st:
                b = bin(n)
                b = b[2:]
                break
            n += 1
        
        return "0"*(len(nums)-len(b))+b