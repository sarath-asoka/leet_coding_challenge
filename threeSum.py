# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 16:01:20 2023

@author: sarat
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        le = set()
        ko = []
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:# and i<j and i<k and j<k:
                        le.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        for i in le:
            ko += list(i),
        return ko
                        
nums = [0,0,0]     
sol = Solution()
print(sol.threeSum(nums))