
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        print(len(set(nums)))
        print(len(nums))
        return len(set(nums)) < len(nums)                   
        
x = [1,2,3,1,1,1]       
sol = Solution()
print(sol.containsDuplicate(x))