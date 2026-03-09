class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapper = {num:i for i, num in enumerate(nums2)}

        pos = [-1 for _ in range(len(nums2))]
        stack = []
        for i in range(len(nums2)-1, -1, -1):
            if not stack:
                stack.append(nums2[i])
                continue
            
            if stack[-1] > nums2[i]:
                pos[i] = stack[-1]
                stack.append(nums2[i])
            else:
                while stack and stack[-1] < nums2[i]:
                    stack.pop()
                if stack:
                    pos[i] = stack[-1]
                stack.append(nums2[i])
        
        res = []
        for num in nums1:
            res.append(pos[mapper[num]])
        return res

            





            
        
            

 