class Solution:
    def lengthOfLongestSubstring(self, s):
        c_index = dict()
        start, max_count = 0, 0
        for end,c in enumerate(s):
            if c in c_index and c_index[c]>=start:
                start = c_index[c] + 1

            c_index[c]=end
            max_count = max(max_count, end-start+1)
        return max_count
