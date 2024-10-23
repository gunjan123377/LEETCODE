class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1

        while r>l:
            curr = numbers[l] + numbers[r]
            if curr==target:
                return [l+1, r+1]
            elif target > curr:
                l+=1
            else:
                r-=1
        else:
            return False


        