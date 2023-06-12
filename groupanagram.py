
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}

        for i in strs:
            si = ''.join(sorted(i))
            
            if si not in table:
                table[si] = []
                
            table[si].append(i)

        return list(table.values())
            


strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
print(sol.groupAnagrams(strs))