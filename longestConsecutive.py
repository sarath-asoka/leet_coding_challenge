# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        cur_max = 0
        cur_count = 0
        prev = None
        for i in nums:
            if prev is not None:
                if prev+1 == i:
                    cur_count += 1
                else:
                    cur_max = max(cur_max, cur_count)
                    cur_count = 1
            else:
                cur_count += 1
            prev = i
        return max(cur_max, cur_count)
        
nums = [0,3,7,2,5,8,4,6,0,1]
sol = Solution()
print(sol.longestConsecutive(nums))