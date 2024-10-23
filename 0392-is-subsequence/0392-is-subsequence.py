class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, n = 0, len(t)
        for c in s:
            while i<n:
                if c == t[i]:
                    i+=1
                    break
                i+=1
            else:
                return False
        return True