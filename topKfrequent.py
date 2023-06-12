
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = list(set(nums))
        n =[]
        f = 0
        
        for i in l:
            for j in nums:
                if i == j:
                    f +=1
            n.append(f)
            f = 0
            
        # print(l)
        # print(n)
        
        while len(n) > k:
            s = min(n)
            x = n.index(s)
            n.pop(x)
            l.pop(x)
            
        return l
            
                    
        
        
        
        
nums = []
k = 0
sol = Solution()
print(sol.topKFrequent(nums, k))        