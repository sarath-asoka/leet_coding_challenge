# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 16:01:20 2023

@author: sarat
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i != j and i < j and numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
        
numbers = [2,7,11,15]
target = 9
sol = Solution()
print(sol.twoSum(numbers, target))