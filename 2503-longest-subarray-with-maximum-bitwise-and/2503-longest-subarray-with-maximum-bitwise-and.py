class Solution:
    def longestSubarray(self, nums):

        max_num = max(nums)
        max_counts, curr_counts = 0, 0
        
        for num in nums:
            if num == max_num:
                curr_counts += 1
                max_counts = max(max_counts, curr_counts)
            else:
                curr_counts = 0
        return max_counts