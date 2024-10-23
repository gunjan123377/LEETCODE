class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda x:x[1])
        left, right = 0, len(nums) -1

        while right > left:
            current_value = sorted_nums[left][1] + sorted_nums[right][1]
            if target == current_value:
                return [sorted_nums[left][0], sorted_nums[right][0]]
            elif target > current_value:
                left+=1
            else:
                right-=1
        return []