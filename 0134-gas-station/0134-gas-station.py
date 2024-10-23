class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        total_gas, start = 0, 0
        for i, (g,c) in enumerate(zip(gas*2, cost*2)):
            if i == start+l:
                return start

            total_gas = total_gas + g - c

            if total_gas<0:
                start = i + 1
                total_gas = 0
        return -1