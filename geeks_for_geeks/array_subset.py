#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        count = Counter(a)
        for n in b:
            if n not in count or count[n] == 0:
                return False
            count[n] -= 1
        return True
