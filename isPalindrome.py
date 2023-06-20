# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 15:46:04 2023

@author: sarat
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        normal_string="".join(ch for ch in s if ch.isalnum()) # exclude all special characters
        normal_string = normal_string.lower()         # Convert to all lower case
        return normal_string[:] == normal_string[::-1] 
        
            
s = "A man, a plan, a canal: Panama"  
sol = Solution()
print(sol.isPalindrome(s))