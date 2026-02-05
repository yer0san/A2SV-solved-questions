class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        least = float('inf')
        d = {num: i for i, num in enumerate(list2)}
        
        for i in range(len(list1)):
            if list1[i] in d:
                least = min(least, i+d[list1[i]])
        res = []
        for i in range(len(list1)):
            if list1[i] in d and i+d[list1[i]] == least:
                res.append(list1[i])
        return res
