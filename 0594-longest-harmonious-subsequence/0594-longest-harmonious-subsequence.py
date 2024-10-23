class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dict001 = {}
        for n in nums:
            if n in dict001:
                dict001[n]+=1
            else:
                dict001[n]=1
        LHS = 0
        for n in dict001:
            if n+1 in dict001:
                LHS = max(LHS, dict001[n] + dict001[n+1])
        return LHS