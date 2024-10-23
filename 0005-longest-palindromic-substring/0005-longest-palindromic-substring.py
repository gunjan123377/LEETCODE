class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_len, res_str = 0, ""
        l = len(s)

        for i in range(l):
            left, right = i, i
            while left>=0 and right<l and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    res_str = s[left:right+1] 
                    res_len = (right - left + 1)
                left-=1
                right+=1

            left, right = i, i+1
            while left>=0 and right<l and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    res_str = s[left:right+1] 
                    res_len = (right - left + 1)
                left-=1
                right+=1

        return res_str

        