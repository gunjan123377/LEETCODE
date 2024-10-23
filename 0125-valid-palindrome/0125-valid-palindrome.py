import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        act_str, rev_str = "", ""
        for char in s.lower():
            if char.isalnum():
                act_str = act_str + char
                rev_str = char + rev_str
        return act_str == rev_str