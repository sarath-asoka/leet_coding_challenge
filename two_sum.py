from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and (nums[i]+nums[j]) == target and i > j:
                    k.append(j)
                    k.append(i)
                    return k
                else:
                    pass
        
nums = [2,7,11,15]
target = 18
sol = Solution()
print(sol.twoSum(nums, target))