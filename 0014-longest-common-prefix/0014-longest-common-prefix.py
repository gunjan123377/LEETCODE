class Solution:
    def longestCommonPrefix(self, strs):

        smallest_str = min(strs, key=len)
        for i, c in enumerate(smallest_str):
            for s in strs:
                if c != s[i]:
                    return smallest_str[:i]
        else:
            return smallest_str       
        