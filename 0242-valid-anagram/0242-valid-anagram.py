class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            if sorted(s) == sorted(t):
                return True
        return False
        